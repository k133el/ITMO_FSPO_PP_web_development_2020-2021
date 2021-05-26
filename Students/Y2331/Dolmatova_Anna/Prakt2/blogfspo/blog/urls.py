from django.urls import path
from . import views #подключение файла контроллеров,описанного в пункте 3
from .views import *

urlpatterns = {
    path('owner/<int:id>/', views.detail),
    path('owner/list', CarOwnerList.as_view()),
    path('car/list/', CarList.as_view()),
    path('car/<int:pk>/', CarDetail.as_view()),
    path('car/update/<int:pk>/', CarUpdate.as_view()),
    path('car/add/', CarCreate.as_view()),
    path('car/delete/<int:pk>/', CarDelete.as_view()),
    path('owner/add/', owner_create),
}


