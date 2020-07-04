from django.db import models
from django.contrib.postgres.fields import ArrayField


class Movies(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    title= models.CharField(max_length=100)
    poster_path= models.CharField(max_length=100)
    backdrop_path= models.CharField(max_length=100)
    original_language= models.CharField(max_length=100)
    original_title= models.CharField(max_length=1000)
    overview= models.CharField(max_length=1000)
    release_date=models.CharField(max_length=100)
    popularity= models.IntegerField()
    vote_count= models.IntegerField()
    video= models.BooleanField()
    adult= models.BooleanField()
    genre_ids = ArrayField(models.IntegerField(),size=10)
    def __str__(self):
        return self.id

    class Meta:
        ordering = ('id',)

class Watchlist(models.Model):
    
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    codename = models.CharField(max_length=100)
    title= models.CharField(max_length=100)
    poster_path= models.CharField(max_length=100)
    backdrop_path= models.CharField(max_length=100)
    original_language= models.CharField(max_length=100)
    original_title= models.CharField(max_length=1000)
    overview= models.CharField(max_length=1000)
    release_date=models.CharField(max_length=100)
    popularity= models.IntegerField()
    vote_count= models.IntegerField()
    video= models.BooleanField()
    adult= models.BooleanField()
    genre_ids = ArrayField(models.IntegerField(),size=10)
    def __str__(self):
        return self.id

    class Meta:
        ordering = ('id',)

