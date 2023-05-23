from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    saludo = 'Bienvenido a Avelinas Centro de Estetica'
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_con_html(request):
    contexto = { }
    http_responde = render(
        request=request,
        template_name='servicios_ofrecidos/base.html',
        context=contexto,
    )
    return http_responde