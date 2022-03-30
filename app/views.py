# from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail


def home(request):
    context = {}
    return render(request, 'app/index.html', context)


def about(request):
    context = {}
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
        first_name = request.POST.get('first-name', False)
        last_name = request.POST.get('last-name', False)
        email = request.POST.get('email', False)
        message = request.POST.get('message', False)
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'message': message
        }
        # send email
        send_mail(
            # subject:
            'message from' + '' + first_name, 
            # message:
            message,
            # from which email
            email,
            # to which email
            ['smkekae1@gmail.com'],


        )
        return render(request, 'app/contact.html', context)

    else:
        return render(request, 'app/contact.html')
