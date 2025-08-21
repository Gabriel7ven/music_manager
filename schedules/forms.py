from django import forms
import datetime

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    
    
class MusicForm(forms.Form):
    CHOICES = [
        ('1', 'SERVICO DE CANTICO'),
        ('2', 'MENSGAEM MUSICAL'),
        ('3', 'OFERTORIO'),
        ('4', 'ARCA DE ORACAO'),
        ('5', 'DISPERSAO DAS CLASSES'), 
        ('6', 'DESPEDIDA'),
    ]
    music_name = forms.CharField(max_length=100)
    reference = forms.CharField(max_length=100)
    number = forms.IntegerField(min_value=0, initial=0)
    moment = forms.ChoiceField(choices=CHOICES, initial='1')
    # sing_date = forms.DateField()