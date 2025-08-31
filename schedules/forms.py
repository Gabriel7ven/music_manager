from django import forms
import datetime
from .models import Music

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)
    
    
from django import forms

class MusicForm(forms.Form):
    CHOICES = [(key, value) for key, value in Music.MOMENTS.items()]
    
    music_name = forms.CharField(
        max_length=100,
        label="Nome da música",
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o nome da música...',
            'style': 'width: 100%;',  # tamanho customizado
        })
    )
    
    reference = forms.CharField(
        max_length=100,
        label="Referência",
        widget=forms.TextInput(attrs={
            'placeholder': 'Referência bíblica ou página do hinário...',
            'style': 'width: 100%; ',
        })
    )
    
    number = forms.IntegerField(
        min_value=0, 
        initial=0,
        label="Número",
        widget=forms.NumberInput(attrs={
            'placeholder': 'Número do hino (se aplicável)...',
            'style': 'width: 100%;',
        })
    )
    
    moment = forms.ChoiceField(
        choices=CHOICES, 
        initial='1',
        label="Momento do programa",
        widget=forms.Select(attrs={
            'style': 'width: 300px;',
        })
    )
    
class UpdateForm(forms.Form):
    CHOICES = [(key, value) for key, value in Music.MOMENTS.items()]
    music_name = forms.CharField(max_length=100)
    reference = forms.CharField(max_length=100)
    number = forms.IntegerField(min_value=0, initial=0)
    moment = forms.ChoiceField(choices=CHOICES, initial='1')