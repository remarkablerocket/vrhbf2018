from django.db import models
from django.conf import settings


class Brewery(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)


class Bar(models.Model):
    name = models.CharField(max_length=200)


class Beer(models.Model):
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    number = models.PositiveSmallIntegerField(null=True, blank=True)
    reserved = models.BooleanField(default=False)
    abv = models.PositiveSmallIntegerField(null=True, blank=True)
    tasting_notes = models.TextField()
    notes = models.TextField()


class UserBeer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    starred = models.BooleanField(default=True)
    tried = models.BooleanField(default=False)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
