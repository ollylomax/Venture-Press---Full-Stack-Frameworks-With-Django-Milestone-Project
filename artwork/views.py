from django.shortcuts import render, redirect

from .models import Artwork
from .forms import ArtworkUpload


def orders_requiring_artwork(request):

    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = ArtworkUpload(request.POST, request.FILES)
        if form.is_valid():
            cust_artwork = Artwork(upload=request.FILES['upload'])
            cust_artwork.save()

            # Redirect to the document list after POST
            return redirect('orders_requiring_artwork')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = ArtworkUpload()  # An empty, unbound form

    # Load documents for the list page
    files = Artwork.objects.all()

    # Render list page with the documents and the form
    context = {'files': files, 'form': form, 'message': message}
    return render(request, "artwork/artwork.html", context)