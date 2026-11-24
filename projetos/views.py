from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from .models import Projeto


class ProjetoList(ListView):
    model = Projeto


class ProjetoDetail(DetailView):
    model = Projeto


def boas_vindas(request):
    return HttpResponse("Bem-vindo ao meu portfolio")