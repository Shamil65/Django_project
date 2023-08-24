from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    my_objects = models.Cats.objects.all()
    return render(request, 'index.html', {'my_objects': my_objects})
