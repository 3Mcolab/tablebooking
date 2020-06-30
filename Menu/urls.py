from django.urls import path
from . import views

app_name='Menu'

urlpatterns =[
    path('menu/',views.MenuPage,name='menu'),
]
