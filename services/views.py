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

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Addition Successful - product added')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request, 'Invalid Form - failed addition')
    else:
        form = ServiceForm()

    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_service(request, service_id):
    """ Edit an existing print service """
    service = get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Edit Successful - changes made')
            return redirect(reverse('service_detail', args=[service.id]))
        else:
            messages.error(request, 'Invalid Form - failed edit')
    else:
        form = ServiceForm(instance=service)

    template = 'services/edit_service.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)


def delete_service(request, service_id):
    """ Delete an existing print service """
    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    messages.success(request, 'Deletion successful - service removed')
    return redirect(reverse('services'))
