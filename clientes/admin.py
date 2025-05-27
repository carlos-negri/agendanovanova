from django.contrib import admin
from django.utils.html import format_html

from clientes.models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    fields = ('nome', 'endereco', 'fone', 'email', 'foto', 'fotografia')
    list_display = ('nome', 'endereco', 'email')
    readonly_fields = ['fotografia']
    search_fields = ('nome', 'fone')

    def fotografia (self,obj):
        if obj.foto:
            return format_html('<img width="75px" src="{}" />', obj.foto.url)
        pass

