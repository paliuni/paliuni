from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default='default.png', blank=True)
    slug = models.SlugField(unique=True)
    facebook = models.URLField(max_length=1000, blank=True)
    linkedin = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return self.name

