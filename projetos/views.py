from django.views.generic import ListView, DetailView
from .models import Projeto

class ProjetoList(ListView):
    model = Projeto

class ProjetoDetail(DetailView):
    model = Projeto
    
