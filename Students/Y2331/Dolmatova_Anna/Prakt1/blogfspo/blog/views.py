from django.shortcuts import render
from django.http import Http404
from .models import *


def detail(request, id):
    try:
        p = CarOwner.objects.get(pk=id)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'detail.html', {'owner': p})
# Create your views here.
