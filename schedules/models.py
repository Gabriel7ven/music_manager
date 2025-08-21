from django.db import models
from django.utils import timezone



class Music(models.Model):
    MOMENTS = {
        '1': 'SERVICO DE CANTICO',
        '2': 'MENSAGEM MUSICAL',
        '3': 'OFERTORIO',
        '4': 'ARCA DE ORACAO',
        '5': 'DISPERSAO DAS CLASSES',       
        '6': 'DESPEDIDA',
        '7': 'HINO FINAL',
    }
    
        
    music_name = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    moment = models.CharField(max_length=200, choices=MOMENTS.items())
    sing_date = models.DateTimeField()

    def get_moment_name(self):
        """Método personalizado para obter o nome do momento"""
        return self.MOMENTS.get(self.moment, 'MOMENTO DESCONHECIDO')
    
    def __str__(self):
        return self.music_name
    
class Moments(models.Model):
    moment = models.CharField(max_length=200)
    
    def __str__(self):
        return self.moment