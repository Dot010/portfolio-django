from django.contrib import admin

from .models import Categoria, Tecnologia, Projeto, Perfil, Contato

admin.site.register(Categoria)
admin.site.register(Tecnologia)
admin.site.register(Perfil)
admin.site.register(Contato)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "destaque")
    search_fields = ("titulo",)
    list_filter = ("categoria", "destaque")