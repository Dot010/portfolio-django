from django.urls import path
from .views import ProjetoList, ProjetoDetail

urlpatterns = [
    path("", ProjetoList.as_view(), name="projeto_list"),
    path("<int:pk>/", ProjetoDetail.as_view(), name="projeto_detail"),
]