from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import ClienteModelForm
from .models import Cliente

class ClientesView(ListView):
    model = Cliente
    template_name = 'clientes.html'


    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ClientesView, self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)


        if qs.count() > 0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem clientes cadastrados!')



class ClienteAddView(SuccessMessageMixin, CreateView):
        model = Cliente
        form_class = ClienteModelForm
        template_name = 'cliente_form.html'
        success_url = reverse_lazy('clientes')
        success_message = "Cliente cadastrado com sucesso!"


class ClienteUpdateView(SuccessMessageMixin, UpdateView):
    model = Cliente
    form_class = ClienteModelForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')
    success_message = "Cliente alterado com sucesso!"



class ClienteDeleteView(SuccessMessageMixin, DeleteView):
        model = Cliente
        template_name = 'cliente_apagar.html'
        success_url = reverse_lazy('clientes')
        success_message = "Cliente apagado com sucesso!"

        def post (self, request, *args, **kwargs):
            self.object = self.get_object()
            success_url = self.get_success_url()
            try:
                return super().post(request, *args, **kwargs)
            except ProtectedError:
                messages.error(request, f'O cliente {self.object} não pode ser excluído. ' 
                                        f'Esse cliente está registrado em agendamentos')
            finally:
                return redirect(success_url)
