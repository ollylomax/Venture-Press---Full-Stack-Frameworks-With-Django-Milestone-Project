from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import ContactForm
from contact.models import Messages

from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mass_mail

from django.conf import settings


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        if request.user.username:
            form['first_name'].initial = request.user.first_name
            form['last_name'].initial = request.user.last_name
            form['email'].initial = request.user.email
            form['user'].initial = request.user

    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            subject = render_to_string('contact/contact_email/contact_email_subject.txt', {'form': form})
            customer_email_body = render_to_string('contact/contact_email/contact_confirmation_email_body.txt', {'form': form})
            company_email_body = render_to_string('contact/contact_email/contact_from_email_body.txt', {'form': form})
            customer_email = (
                subject,
                customer_email_body,
                settings.VENTURE_PRESS_EMAIL,
                [form['email'].value()]
            )
            company_email = (
                subject,
                company_email_body,
                settings.VENTURE_PRESS_EMAIL,
                [settings.VENTURE_PRESS_EMAIL]
            )
            try:
                send_mass_mail((customer_email, company_email), fail_silently=False)
            except Exception as e:
                messages.error(request, f'Error: {e}')
                return HttpResponse(status=500)
            return redirect('success')
 
    return render(request, "contact/contact.html", {'form': form})


def success(request):
    messages.success(request, "Your contact request has been received")
    return render(request, "contact/success.html")


def edit_message(request, message_id):
    """ Edit an existing print service """
    message = get_object_or_404(Messages, pk=message_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            messages.success(request, 'Edit Successful - changes made')
            return redirect(reverse('past_message', args=[message.id]))
        else:
            messages.error(request, 'Invalid Form - failed edit')
    else:
        form = ContactForm(instance=message)

    template = 'contact/edit_message.html'
    context = {
        'form': form,
        'message': message,
    }

    return render(request, template, context)

