from django.urls import path

from . import views

app_name = 'schedules'
urlpatterns = [
    path("", views.index, name='index'),
    path("calendar/", views.get_calendar, name='calendar'),
    path("contact/", views.get_name, name='contact'),
    path("music/<int:year>/<int:month>/<int:day>", views.get_music, name='music'),
    path("update/<int:music_id>/", views.update, name='update'),
]