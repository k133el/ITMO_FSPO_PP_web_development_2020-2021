from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import Http404
from .models import *
from .forms import *

def detail(request, id):
    try:
        p = CarOwner.objects.get(pk=id)
    except CarOwner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'detail.html', {'owner': p})


class CarOwnerList(ListView):
    model = CarOwner
    template_name = 'CarOwner_list.html'


class CarList(ListView):
    model = Car
    template_name = 'Car_list.html'


class CarDetail(DetailView):
    model = Car
    template_name = 'CarDetail.html'


class CarUpdate(UpdateView):
    model = Car
    fields = ['state_number', 'mark', 'model', 'color']
    template_name = 'Car_Update.html'
    success_url = '/car/list/'


def owner_create(request):
    # dictionary for initial data with
    # field names as keys
    context = {}


    # add the dictionary during initialization
    form = CarOwnerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "CarOwner_Create.html", context)


class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    template_name = 'create_car.html'
    success_url = '/car/list'


class CarDelete(DeleteView):
    model = Car
    template_name = 'delete_car.html'
    success_url = '/car/list'

