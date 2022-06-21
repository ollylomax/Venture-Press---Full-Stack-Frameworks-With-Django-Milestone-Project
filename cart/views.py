from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from services.models import Service

# Create your views here.


def cart(request):
    """ Route to return the Index page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ View to add quantity of chosen product to cart """

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
    """Amend the quantity of the chosen product """

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
    """Remove the item from the shopping bag"""

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