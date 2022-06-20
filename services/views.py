from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Service

# Create your views here.


def all_services(request):
    """ Route for all services, including sorting and search queries """

    services = Service.objects.all()
    query = None

    if request.GET:
        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(request, "You must type something in the Search field")
                return redirect(reverse('services'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            services = services.filter(queries)

    context = {
        'services': services,
        'query': query,
    }

    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    """ Route to show service details """

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_detail.html', context)