from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def eliminar_objeto(request, id2):
    Especialidad = models.Especialidad.objects.get(id=int(id2))
    Especialidad.delete()
    saludo = 'Eliminado con exito'
    pagina_html = HttpResponse(saludo)
    return pagina_html

def crear_objeto(request):
    Objeto = models.Esppecialidad(especialidad = 'pedicuria')
    Objeto.save()
    saludo = 'Especialdiad creada con exito'
    pagina_html = HttpResponse(saludo)
    return pagina_html
