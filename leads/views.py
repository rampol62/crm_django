from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
# Create your views here.

def lead_list(request):
    lideres = Lead.objects.all()
    contexto01 = {
        "lideres": lideres
    }
    context = {
        "name":"joe",
        "age":35
    }
    return render(request,"leads/lead_list.html",contexto01)


def lead_detail(request, pk):
    print(pk)
    lider = Lead.objects.get(id=pk)
    print(lider)
    contexto = {
        "lider": lider
    }
    return render(request,"leads/lead_detail.html",contexto)

