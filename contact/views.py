from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail

from django.conf import settings


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
        if request.user.username:
            form['first_name'].initial = request.user.first_name
            form['last_name'].initial = request.user.last_name
            form['email'].initial = request.user.email

    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            subject = render_to_string('contact/contact_email/contact_email_subject.txt', {'form': form})
            body = render_to_string('contact/contact_email/contact_email_body.txt', {'form': form})
            send_mail(
                subject,
                body,
                form['email'].value(),
                [settings.VENTURE_PRESS_EMAIL]
            )
            return redirect('success')
 
    return render(request, "contact/contact.html", {'form': form})


def success(request):
    messages.success(request, "Your contact request has been received")
    return render(request, "contact/success.html")