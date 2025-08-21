from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('schedules/', include('schedules.urls')),
    path('admin/', admin.site.urls),
]
