from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages

from checkout.models import Order
from accounts.models import UserProfile

from .models import Artwork
from .forms import ArtworkUpload


def orders_requiring_artwork(request):

    # Init empty form
    form = ArtworkUpload()

    order_filter = get_object_or_404(UserProfile, user=request.user)

    orders = order_filter.orders.all()

    # All files to be rendered in template
    files = Artwork.objects.all()

    # Render the artwork template with context
    context = {'files': files, 'form': form, 'orders': orders}
    return render(request, "artwork/artwork.html", context)


def upload_artwork(request, order_number):

     # Handle file upload
    if request.method == 'POST':
        files = Artwork.objects.all()
        form = ArtworkUpload(request.POST, request.FILES)
        user = get_object_or_404(UserProfile, user=request.user)
        order = get_object_or_404(Order, order_number=order_number)

        form_data = {
            'user': user,
            'order': order,
            'upload': request.FILES['upload'],
        }

        cust_artwork = ArtworkUpload(form_data)
        print(cust_artwork)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'NOPE')
            # print(form.errors.as_data())

            # return redirect('orders_requiring_artwork')

        context = {'files': files, 'form': form}
        return render(request, "artwork/artwork.html", context)