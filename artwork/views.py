from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    reverse,
)

from django.contrib import messages

from checkout.models import Order
from checkout.forms import OrderForm
from accounts.models import UserProfile

from .models import Artwork
from .forms import ArtworkUpload


def orders_requiring_artwork(request):
    """
    Orders requiring artwork view initialising an empty ArtworkUpload form
    and an empty OrderForm from the respective imported models. Get the current
    user from the session then filter the Order object by the user and by the
    has_artwork boolean field and save to orders variable. Set initial field
    values for the foreign key fields from the Artwork model and filter model
    by user session to a files variable. Pass both forms, and both variables
    to the template.
    """

    # Init empty form
    form = ArtworkUpload()
    order_form = OrderForm()
    
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.filter(user_profile=profile, has_artwork=False)

    form['user'].initial = request.user

    for order in orders:  
        form['order'].initial = order

    # File urls rendered to template
    files = Artwork.objects.filter(user=profile)

    # Render the artwork template with context
    context = {
        'files': files,
        'form': form,
        'orders': orders,
        'order_form': order_form,
        }

    return render(request, "artwork/artwork.html", context)


def upload_artwork(request, order_number):
    """
    View to upload artwork by receiving order_number from the template, get the 
    order from the order Object by order_number and save it to a variable used
    to instantiate an OrderForm. If request is POST then instantiate an
    ArtworkUpload form with submitted fields and file into a variable and save
    if valid. Set a variable for an uncommitted save of OrderForm, update the
    has_artwork field to true and save. Pass both forms and order variable back
    to the template.
    """
    order = get_object_or_404(Order, order_number=order_number)
    order_form = OrderForm(instance=order)

    # Handle file upload
    if request.method == 'POST':
        files = Artwork.objects.all()
        form = ArtworkUpload(request.POST, request.FILES)
        form['order'].initial = order

        # Upload file and change has_artwork boolean in corresponding order
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

