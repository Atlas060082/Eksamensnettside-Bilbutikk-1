# biler/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Bil

class BilListe(ListView):
    model = Bil

class BilOpprett(CreateView):
    model = Bil
    fields = "__all__"
    success_url = "/biler/"

class BilOppdater(UpdateView):
    model = Bil
    fields = "__all__"
    success_url = "/biler/"

class BilSlett(DeleteView):
    model = Bil
    success_url = "/biler/"
