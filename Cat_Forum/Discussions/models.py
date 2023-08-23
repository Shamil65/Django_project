from django.db import models

class Cats(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title