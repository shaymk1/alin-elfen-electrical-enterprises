# from multiprocessing import context
from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
# from django.views.generic import TemplateView


def home(request):
    return render(request, 'app/index.html')
    
def about(request):
    about_us = About.objects.all()
    context = {
        'about_us': about_us
    }
    return render(request, 'app/about.html', context)


def services(request):
    services = Services.objects.all()
    context = {
        'services': services
    }
    return render(request, 'app/services.html', context)


def contact(request):
    if request.method == 'POST':
        # If key is in request.POST the key variable will be equal to it, if not, then it will be equal to False.

        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # send email
        send_mail(
            (f"message from {first_name} {last_name}"),
            message,
            # from sender which is in settings.py
            email,
            # to which email
            ['smkekae1@gmail.com'],
            fail_silently=False,
        )

        context = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'message': message
        }

        

       
        return render(request, 'app/contact.html', context)
    else:
        return render(request, 'app/contact.html')

     ## messages.success(     request, 'your message has been submitted successfully, we will get back to you as soon as we can!')
        # return HttpResponseRedirect('/home/')
        # return HttpResponseRedirect(reverse('home'))
        
