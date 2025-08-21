from django.shortcuts import render
import datetime
import calendar
from django.http import HttpResponseRedirect, HttpResponse


from .forms import ContactForm, MusicForm
from django.core.mail import send_mail

from .models import Music
from datetime import date
app_name = 'schedules'

def index(request):
    return render(request, "schedules/index.html")

def get_calendar(request):
    # Obter parâmetros da URL ou usar a data atual
    year = int(request.GET.get('year', datetime.datetime.now().year))
    month = int(request.GET.get('month', datetime.datetime.now().month))
    
    # Validar os valores
    if month < 1:
        month = 12
        year -= 1
    elif month > 12:
        month = 1
        year += 1
    
    # Calcular datas para navegação
    prev_month = month - 1 if month > 1 else 12
    prev_year = year if month > 1 else year - 1
    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1
    
    # Gerar semanas do calendário
    weeks = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    
    context = {
        'weeks': weeks,
        'month': month,
        'month_name': month_name,
        'year': year,
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year,
    }
    
    return render(request, "schedules/calendar.html", context)



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        

        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["sender"]
            cc_myself = form.cleaned_data["cc_myself"]

            recipients = ["gabriel.oficial@yahoo.com"]
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponse("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, "schedules/contact.html", {"form": form})


def get_music(request, year, month, day):
    # Filtrar músicas pela data específica (day, month, year)
    sing_date = date(year, month, day)
    musics_of_day = Music.objects.filter(sing_date=sing_date)
    
    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            music_name = form.cleaned_data['music_name']
            reference = form.cleaned_data['reference']
            number = form.cleaned_data['number']
            moment = form.cleaned_data['moment']
            
            # Criar e salvar a música com a data correta
            Music.objects.create(
                music_name=music_name,
                reference=reference,
                number=number,
                moment=moment,
                sing_date=sing_date
            )
            
            # Atualizar a lista após adicionar nova música
            musics_of_day = Music.objects.filter(sing_date=sing_date)
            form = MusicForm()
            
            return render(request, 'schedules/music_form.html', {
                'form': form, 
                'musics': musics_of_day,
                'day': day,
                'month': month,
                'year': year
            }) 
        else:
            return HttpResponse('Erro ao salvar objeto no banco de dados')
    else:
        form = MusicForm()
        
    return render(request, 'schedules/music_form.html', {
        'form': form, 
        'musics': musics_of_day,
        'day': day,
        'month': month,
        'year': year
    })