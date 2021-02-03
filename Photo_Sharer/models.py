from django.db import models

# Create your models here.


class Image (models.Model):
    photo = models.ImageField(upload_to='images')
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
