from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Nothing in your bag")
        return redirect(reverse('services'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51L8M0hHB8OpqVDbT2n0RMtNLfwET8tHCksJXt6QzFgTEHHLl80jOmGRPuH532pMSuyOGHjOt5iFAEVWEmArTLCtW00FrPlxH7n',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)