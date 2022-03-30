# from multiprocessing import context
from django.shortcuts import render


def home(request):
  context = {}
  return render(request, 'app/index.html',context )


def about(request):
  context = {}
  return render(request, 'app/about.html', context)


def services(request):
  context = {}
  return render(request, 'app/services.html', context)


def contact(request):
  context = {}
  return render(request, 'app/contact.html', context)
