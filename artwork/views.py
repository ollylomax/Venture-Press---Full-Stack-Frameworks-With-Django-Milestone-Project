from django.shortcuts import render, redirect

from .models import Artwork
from .forms import ArtworkUpload


def orders_requiring_artwork(request):

    # Handle file upload
    if request.method == 'POST':
        form = ArtworkUpload(request.POST, request.FILES)
        if form.is_valid():
            cust_artwork = Artwork(upload=request.FILES['upload'])
            cust_artwork.save()

            # Redirect to orders_requiring_artwork view
            return redirect('orders_requiring_artwork')
    else:
        # Init empty form
        form = ArtworkUpload()

    # All files to be rendered in template
    files = Artwork.objects.all()

    # Render the artwork template with context
    context = {'files': files, 'form': form, 'message': message}
    return render(request, "artwork/artwork.html", context)