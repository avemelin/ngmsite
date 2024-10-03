from .models import Artiles
from django.forms import ModelForm, TextInput, Textarea

class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['name', 'contact', 'text']

        widgets = {
            'name': TextInput(attrs = {
                'placeholder': 'Имя',
                'class': 'form-control',
            }),

            'contact': TextInput(attrs={
                'placeholder': 'Телефон',
                'class': 'form-control'

            }),

            'text': Textarea(attrs={
                'placeholder': 'Комментарий',
                'class': 'form-control'

            }),

        }