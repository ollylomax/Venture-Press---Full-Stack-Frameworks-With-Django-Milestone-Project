from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Category, Service
from .forms import ServiceForm
from .custom_decorators import superuser_required


def all_services(request):
    """ Route for all services, including sorting and search queries. Get all
    services from Service object, initialise variables with None values. If
    category is in GET request, filter services object by category selected in
    template and reassign variable. If query is in GET request then assign
    requested query to variable and filter service names and descriptions by
    it, then reassign original variable with the filtered results. Pass
    service variable, categories and query back to the template."""

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
                messages.error(
                    request, "You must type something in the Search field")
                return redirect(reverse('services'))
            
            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            services = services.filter(queries)

    context = {
        'services': services,
        'query': query,
        'categories': categories,
    }

    return render(request, 'services/services.html', context)


def service_detail(request, service_id):
    """ Route to show service details by receiving service id from path, using
    it to get the corresponding object from the Service model and assigning to
    a variable. Pass the variable back to the template. """

    service = get_object_or_404(Service, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'services/service_detail.html', context)

# Require session decorator from django decorators.
@login_required
# Require superuser decorator from my custom decorators.
@superuser_required
def add_service(request):
    """ View to create a new print service, if request is POST initialise a
    ServiceForm with the post and file requests, and if valid then save to
    variable. If invalid then send toast message and reverse to service detail
    page passing back the service id.

    If request is GET then initialise an empty ServiceForm into the same
    variable name, pass to the template and render.
    """

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


# Require session decorator from django decorators.
@login_required
# Require superuser decorator from my custom decorators.
@superuser_required
def edit_service(request, service_id):
    """ Edit an existing print service by receiving service id from url path,
    searching Service model using the service id and returning the service to a
    variable. Instantiate a ServiceForm with the variable set above and pass
    both the form and the variable to the template.
    
    If request is POST then check form for validity and if valid then save,
    sending a toast success message and reversing to service detail template
    passing the service id back as an argument. If invalid then send toast
    error message.
    """

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


# Require session decorator from django decorators.
@login_required
# Require superuser decorator from my custom decorators.
@superuser_required
def delete_service(request, service_id):
    """ Delete an existing print service by receiving service id from url path,
    searching Service model using the service id and returning the service to a
    variable. Delete the service, send toast success message and reverse to
    service view.
    """

    service = get_object_or_404(Service, pk=service_id)
    service.delete()
    messages.success(request, 'Deletion successful - service removed')

    return redirect(reverse('services'))
