
from django.contrib import admin
from django.db import models
from core.models import Evento,Usuarios

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_evento','data_criacao')
    list_filter = ('titulo',)

admin.site.register(Evento, EventoAdmin)
admin.site.register(Usuarios)
