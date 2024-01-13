from django.db import models
import os 
import uuid

def upload_image_formated(self, instance, filename):
    return f'{str(uuid.uuid4())}-{filename}'

class Article(models.Model):
    title = models.CharField('Título', max_length=200, blank=True, null=True)
    subtitle = models.CharField('Sub Título', max_length=300, blank=True, null=True)
    author = models.CharField('Autor', max_length=100, blank=True, null=True)
    photo = models.ImageField('Foto', upload_to=upload_image_formated, blank=True, null=True)
    created = models.DateTimeField('Criado_em', auto_now_add=False, auto_now=False)
    class Meta:
        ordering = ('pk',)
    def __str__(self):
        return '{} - {}'.format(self.pk, self.title)
