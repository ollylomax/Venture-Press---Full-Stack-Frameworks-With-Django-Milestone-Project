from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from services.models import Service


def cart(request):
    """ Simple route to render the cart template """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ View to add or update the quantity of chosen services to cart by receiving
    item id from the template, using it to get the corresponding service and
    adding or updating their quantity to the cart variable then updating the
    session. Set a variable for the path from POST and redirect to previous path
    after adding/updating.
    """

    service = Service.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    path = request.POST.get('path')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {service.name} quantity to {cart[item_id]}x')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {quantity}x {service.name} to your bag')

    request.session['cart'] = cart
    return redirect(path)


def quantity_amend(request, item_id):
    """View to amend the quantity of the chosen product by receiving the item
    id from the template, getting the corresponding servie from the Service
    object and saving it to a variable. Get the quantity from the POST request
    and the cart from session if it exists, else create an empty object. Use
    conditional to update or delete services from the cart then update the cart
    session and redirect to cart view."""

    quantity = int(request.POST.get('quantity'))
    service = Service.objects.get(pk=item_id)
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {service.name} quantity to {cart[item_id]}x')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed all {service.name} from your bag')

    request.session['cart'] = cart
    return redirect(reverse('cart'))


def delete_from_cart(request, item_id):
    """View to remove the chosen product by receiving the item id from the
    template, getting the corresponding servie from the Service object and
    saving it to a variable. Get the cart from session if it exists, else
    create an empty object. Delete service from the cart then update the cart
    session."""

    cart = request.session.get('cart', {})
    service = Service.objects.get(pk=item_id)
    
    try:
        cart.pop(item_id)
        messages.success(request, f'Removed all {service.name} from your bag')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error when removing item: {e}')
        return HttpResponse(status=500)