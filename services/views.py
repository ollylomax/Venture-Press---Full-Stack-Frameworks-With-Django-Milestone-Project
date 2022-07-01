from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Category, Service
from .forms import ServiceForm


def all_services(request):
    """ Route for all services, including sorting and search queries """

    services = Service.objects.all()
    query = None
    categories = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            services = services.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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
        'categories': categories,
    }

    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    """ Route to show service details """

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_detail.html', context)


def add_service(request):
    """ Create a new print service """
    form = ServiceForm()
    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)