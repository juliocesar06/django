from django.shortcuts import render
from core.models import Evento

# Create your views here.
def lista_eventos(request):
    evento = Evento.objects.all()
    dado = {'eventos': evento}
    return render(request, 'agenda.html',dado)



