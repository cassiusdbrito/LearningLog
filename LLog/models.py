from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    '''Assunto que o usuário quer estudar'''

    text = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        '''Devolve uma representação do modelo em string'''
        return self.text
    
class Entry(models.Model):
    '''Anotação sobre o assunto'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        return self.text[:50] + "..."