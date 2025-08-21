from django import forms
import datetime
from .models import Music

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    
    
class MusicForm(forms.Form):
    CHOICES = [(key, value) for key, value in Music.MOMENTS.items()]
    music_name = forms.CharField(max_length=100)
    reference = forms.CharField(max_length=100)
    number = forms.IntegerField(min_value=0, initial=0)
    moment = forms.ChoiceField(choices=CHOICES, initial='1')
    # sing_date = forms.DateField()
    
class UpdateForm(forms.Form):
    CHOICES = [(key, value) for key, value in Music.MOMENTS.items()]
    music_name = forms.CharField(max_length=100)
    reference = forms.CharField(max_length=100)
    number = forms.IntegerField(min_value=0, initial=0)
    moment = forms.ChoiceField(choices=CHOICES, initial='1')