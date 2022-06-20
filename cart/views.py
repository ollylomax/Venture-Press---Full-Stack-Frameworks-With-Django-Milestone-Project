from django.shortcuts import render

# Create your views here.


def cart(request):
    """ Route to return the Index page """

    return render(request, 'cart/cart.html')
