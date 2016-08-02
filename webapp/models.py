from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
from django.db.models.deletion import CASCADE


class Tour(models.Model):
    date= models.DateField()
    location=models.CharField(max_length=20)
    details=models.FileField()
    owner = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('toursdetails',kwargs={'pk':self.pk})


    def __str__(self):
        return str(self.date)


class Picture(models.Model):
    name=models.CharField(max_length=20)
    tour=models.ForeignKey(Tour,on_delete=CASCADE)
    pic = models.ImageField()
    owner = models.ForeignKey(User)

    def __str__(self):
        return str(self.name)


#logout html page
#user registration form
#manual form
#create picture without taking tour manually
#files must beuploaded to a userfolder....and pictures to corresponding tours folder


