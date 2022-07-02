from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm
from contact.models import Messages


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


@login_required
def message_centre(request):
    """ Message centre page view """
    
    if not Messages.objects.filter(user=request.user).exists():
        user_messages = None
    else:
        user_messages = get_list_or_404(Messages, user=request.user)

    template = 'accounts/messages.html'
    context = {
        'user_messages': user_messages,
    }

    return render(request, template, context)


@login_required
def past_message(request, message_id):
    message = get_object_or_404(Messages, pk=message_id)

    if request.user == message.user:

        template = 'accounts/past_message.html'
        context = {
            'message': message,
        }

        return render(request, template, context)
    else:
        messages.error(request, 'Invalid Message')
        return redirect(message_centre)
