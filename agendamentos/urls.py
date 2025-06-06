from django.urls import path

from .views import AgendamentosView, AgendamentoAddView, AgendamentoUpdateView, AgendamentoDeleteView, \
    AgendamentoInLineEditView, AgendamentoExibir

urlpatterns = [
    path('agendamentos', AgendamentosView.as_view(), name='agendamentos'),
    path('agendamento/adicionar/', AgendamentoAddView.as_view(), name='agendamento_adicionar'),
    path('<int:pk>/agendamento/editar/', AgendamentoUpdateView.as_view(), name='agendamento_editar'),
    path('<int:pk>/agendamento/apagar/', AgendamentoDeleteView.as_view(), name='agendamento_apagar'),
    path('<int:pk>/agendamento/inline', AgendamentoInLineEditView.as_view(), name='agendamento_inline'),
    path('<int:pk>/agendamento/exibir/', AgendamentoExibir.as_view(), name='agendamento_exibir'),
]