from cProfile import label
from django import forms
from tempus_dominus.widgets import DatePicker
from passagens.classe_viagens import tipo_de_classe
from datetime import datetime

class PassagemForms(forms.Form):
    origem = forms.CharField(label = 'Origem', max_length=100)
    destino = forms.CharField(label = 'Destino', max_length=100)
    data_ida = forms.DateField(label = 'Ida', widget=DatePicker())
    data_volta = forms.DateField(label = 'Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data de pesquisa', disabled=True, initial=datetime.today)
    classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipo_de_classe)
    informacoes = forms.CharField(
        label='Informações extras',
        max_length=200,
        widget=forms.Textarea(),
        required=False
    )
    email = forms.EmailField(max_length=100)

    def clean_origem(self):
        origem = self.cleaned_data.get('origem')
        if any(char.isdigit() for char in origem):
            raise forms.ValidationError('Origem inválida: Não inclua números')
        else:
            return origem