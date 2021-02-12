from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Image (models.Model):
    photo = models.ImageField(upload_to='images')
    date_posted = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'pk': self.pk})
