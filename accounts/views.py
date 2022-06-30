from django.shortcuts import render


def profile(request):
    """ Profile page view """

    template = 'accounts/profile.html'
    context = {}

    return render(request, template, context)
