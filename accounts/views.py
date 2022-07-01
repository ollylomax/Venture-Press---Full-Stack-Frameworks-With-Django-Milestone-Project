from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Profile page view """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update Successful - changes made')
        else:
            messages.error(request, 'Invalid Form - failed to update')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'accounts/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def order_history(request):
    """ Order History page view """
    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    template = 'accounts/order_history.html'
    context = {
        'orders': orders,
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def past_order(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    template = 'accounts/past_order.html'
    context = {
        'order': order,
    }

    return render(request, template, context)