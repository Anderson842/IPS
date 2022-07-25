from django.template import Template, Context
from django.http import HttpResponse

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
        

def saludo(request):
    
    p1=Persona("Anderson", "Rivera")
    lenguajes =["Python", "JavaScript", "Java"]
    doc_externo = open(r"C:\Users\Usuario\Desktop\ProyDjango\IPS\IPS\Plantillas\plantilla1.html")
    plt=Template(doc_externo.read())
    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "lenguajes":lenguajes})
    documento=plt.render(ctx)


    return HttpResponse(documento)