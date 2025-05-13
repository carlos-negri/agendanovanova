from django import forms
from django.forms import inlineformset_factory

from servicos.models import Servico, ProdutosServico



class ServicoModelForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'


        error_messages = {
            'nome': {'required': 'O nome do serviço é um campo obrigatório.', 'unique':'Serviço já cadastrado'},
            'preco': {'required': 'O preço do serviço é um campo obrigatório.'},
            'descricao': {'required': 'A descrição do serviço é um campo obrigatório.'},
        }

ProdutosServicoInLine = inlineformset_factory(Servico, ProdutosServico, fk_name='servico',
                                              fields=('produto', 'quantidade'), extra=1, can_delete=True)
##fk_name especifica qual fk vai ser utilizada
##nro de formularios que vai mostrar de cada vez
