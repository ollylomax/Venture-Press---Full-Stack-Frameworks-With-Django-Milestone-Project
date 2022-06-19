from django.shortcuts import render

# Create your views here.


def index(request):
    """ Route to return the Index page """

    return render(request, 'home/index.html')
