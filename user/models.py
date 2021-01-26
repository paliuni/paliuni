from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    mobile = models.CharField(max_length=12)
    message = models.TextField()
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.name
