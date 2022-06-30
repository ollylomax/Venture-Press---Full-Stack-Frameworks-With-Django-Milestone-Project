from django.shortcuts import get_object_or_404, render, redirect, reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from services.models import Service
from accounts.models import UserProfile
from accounts.forms import UserProfileForm
from cart.contexts import cart_contents

import stripe
import json


@require_POST
def checkout_cache(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Processing Failed. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
            'city': request.POST['city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'phone_number': request.POST['phone_number'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.payment_id = pid
            order.cart_instance = json.dumps(cart)
            order.save()
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

        # Attempt to prefill the form with any info the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'address_line1': profile.default_address_line1,
                    'address_line2': profile.default_address_line2,
                    'city': profile.default_city,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                    'phone_number': profile.default_phone_number,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
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

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Link order with user profile
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_address_line1': order.address_line1,
                'default_address_line2': order.address_line2,
                'default_city': order.city,
                'default_county': order.county,
                'default_postcode': order.postcode,
                'default_country': order.country,
                'default_phone_number': order.phone_number,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

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