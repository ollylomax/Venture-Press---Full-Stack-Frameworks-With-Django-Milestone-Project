from django.shortcuts import render, redirect

# Create your views here.


def cart(request):
    """ Route to return the Index page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ View to add quantity of chosen product to cart """

    quantity = int(request.POST.get('quantity'))
    path = request.POST.get('path')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(path)