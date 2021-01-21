from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

# Create your views here.


def lead_list(request):
    lideres = Lead.objects.all()
    contexto01 = {
        "lideres": lideres
    }
    # context = {
    #     "name": "joe",
    #     "age": 35
    # }
    return render(request, "leads/lead_list.html", contexto01)


def lead_detail(request, pk):
    print(pk)
    lider = Lead.objects.get(id=pk)
    print(lider)
    contexto = {
        "lider": lider
    }
    return render(request, "leads/lead_detail.html", contexto)


def lead_create(request):
    # print(request.POST)
    forma = LeadModelForm()
    if request.method == "POST":
        forma = LeadModelForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect("/leads")
    contexto = {
        "forma": forma
    }
    return render(request, "leads/lead_create.html", contexto)


def lead_update(request, pk):
    lider = Lead.objects.get(id=pk)
    forma = LeadModelForm(instance=lider)
    if request.method == "POST":
        forma = LeadModelForm(request.POST, instance=lider)
        if forma.is_valid():
            forma.save()
            return redirect("/leads")
    contexto = {
        "forma": forma,
        "lider": lider
    }
    return render(request, "leads/lead_update.html", contexto)


def lead_delete(request, pk):
    lider = Lead.objects.get(id=pk)
    lider.delete()
    return redirect("/leads")


# def lead_create(request):
#     # print(request.POST)
#     forma = LeadForm()
#     if request.method == "POST":
#         print('Se recibio un requerimiento de Post')
#         forma = LeadForm(request.POST)
#         if forma.is_valid():
#             print('La forma es Valida')
#             print(forma.cleaned_data)
#             first_name = forma.cleaned_data['first_name']
#             last_name = forma.cleaned_data['last_name']
#             age = forma.cleaned_data['age']
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 age = age,
#                 agent = agent
#             )
#             print("El lider a sido Creado")
#             return redirect("/leads")
#     contexto = {
#         "forma":LeadForm()
#     }
#     return render(request,"leads/lead_create.html",contexto)
