from cProfile import label
from django import forms
from tempus_dominus.widgets import DatePicker
from passagens.classe_viagens import tipo_de_classe

class PassagemForms(forms.Form):
    origem = forms.CharField(label = 'Origem', max_length=100)
    destino = forms.CharField(label = 'Destino', max_length=100)
    data_ida = forms.DateField(label = 'Ida', widget=DatePicker())
    data_volta = forms.DateField(label = 'Volta', widget=DatePicker())
    classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipo_de_classe)
