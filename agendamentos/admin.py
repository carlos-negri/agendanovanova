from django.contrib import admin

from agendamentos.models import Agendamento


@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('horario', 'cliente', 'funcionario', 'valor')
    search_fields = ('cliente', 'funcionario')
    list_filter = ('cliente', 'servico')