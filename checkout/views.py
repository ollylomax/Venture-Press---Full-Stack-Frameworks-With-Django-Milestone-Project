from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents
from .models import Order, OrderLineItem
from services.models import Service

import stripe


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'address_line1': request.POST['street_address1'],
            'address_line2': request.POST['street_address2'],
            'city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'phone_number': request.POST['phone_number'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, quantity in cart.items():
                try:
                    service = get_object_or_404(Service, pk=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        service=service,
                        quantity=quantity,
                    )
                    order_line_item.save()

                except Service.DoesNotExist:
                    messages.error(request, (
                        "Service Not Found")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checked_out', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Nothing in your bag")
            return redirect(reverse('services'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checked_out(request, order_number):
    """
    Handler for successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Thank you for your Order! \
        Your order number is {order_number}. We have sent a \
        confirmation email to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checked_out.html'
    context = {
        'order': order,
    }

    return render(request, template, context)