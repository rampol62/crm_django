from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationform

# Create your views here.

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationform

    def get_success_url(self):
        return reverse("login")



class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


def landing_page(request):
    return render(request, "landing.html")


class LeadListView(generic.ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "lideres"


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


class LeadDetailView(generic.DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lider"   


def lead_detail(request, pk):
    print(pk)
    lider = Lead.objects.get(id=pk)
    print(lider)
    contexto = {
        "lider": lider
    }
    return render(request, "leads/lead_detail.html", contexto)

class LeadCreateView(generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


def lead_create(request):
    # print(request.POST)
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    contexto = {
        "form": form
    }
    return render(request, "leads/lead_create.html", contexto)


class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm
    context_object_name = "lider" 

    def get_success_url(self):
        return reverse("leads:lead-list")

def lead_update(request, pk):
    lider = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lider)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lider)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    contexto = {
        "form": form,
        "lider": lider
    }
    return render(request, "leads/lead_update.html", contexto)

class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


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
