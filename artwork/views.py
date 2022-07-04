from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, reverse
from django.contrib import messages

from checkout.models import Order
from checkout.forms import OrderForm
from accounts.models import UserProfile

from .models import Artwork
from .forms import ArtworkUpload


def orders_requiring_artwork(request):

    # Init empty form
    form = ArtworkUpload()
    order_form = OrderForm()
    
    order_filter = get_object_or_404(UserProfile, user=request.user)
    user_orders = order_filter.orders.all()
    orders = get_list_or_404(user_orders, has_artwork=False)

    form['user'].initial = request.user

    for order in orders:  
        form['order'].initial = order

    # File urls rendered to template
    files = Artwork.objects.all()

    # Render the artwork template with context
    context = {
        'files': files,
        'form': form,
        'orders': orders,
        'order_form': order_form,
        }

    return render(request, "artwork/artwork.html", context)


def upload_artwork(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    order_form = OrderForm(instance=order)

     # Handle file upload
    if request.method == 'POST':
        files = Artwork.objects.all()
        form = ArtworkUpload(request.POST, request.FILES)
        form['order'].initial = order

        if form.is_valid():           
            artworks = form.save()
            artworks.order = order
            artworks.save()
            update_order = order_form.save(commit=False)
            update_order.has_artwork = True
            update_order.save()
            messages.success(request, 'Your Artwork has been Successfully Received')

            return redirect(reverse('orders_requiring_artwork'))

        else:
            messages.error(request, 'Issue when Uploading Artwork')
            print(form.errors.as_data())
        
        context = {
            'files': files,
            'form': form,
            'order': order,
            'order_form': order_form}

        return render(request, "artwork/artwork.html", context)

