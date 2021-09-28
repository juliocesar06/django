from django.contrib import admin
from django.urls import path,include
from core import views

#admin.autodiscover()
urlpatterns =[
    path('',views.lista_eventos),
]
