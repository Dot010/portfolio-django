from django.urls import path

from .views import ProjetoDetail, ProjetoList, boas_vindas

urlpatterns = [
    path("", ProjetoList.as_view(), name="projeto_list"),
    path("<int:pk>/", ProjetoDetail.as_view(), name="projeto_detail"),
    path("boas-vindas/", boas_vindas, name="boas_vindas"),
]