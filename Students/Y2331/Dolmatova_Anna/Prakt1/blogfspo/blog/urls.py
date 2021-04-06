from django.urls import path
from . import views #подключение файла контроллеров,описанного в пункте 3
urlpatterns = [
    # path('articles/2003/', views.special_case_2003), #пример вызова контроллера (функции) с именем "special_case_200" из файда views
    path('owner/<int:id>/', views.detail), #пример вызова контроллера (функции) с именем "year_archive" из файда views и передачи в него переменной "year"
]

