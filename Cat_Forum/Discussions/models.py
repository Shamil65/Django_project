from django.db import models

class Cats(models.Model):
    img = models.ImageField('Изображение кота')
    publication_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    description = models.TextField(max_length=1000)
