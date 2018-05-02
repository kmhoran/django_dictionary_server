from django.db import models

class Word(models.Model):
    name = models.CharField(max_length=150)

class Definition(models.Model):
    part_of_speech = models.CharField(max_length=100)
    definition = models.CharField(max_length=500)
    word = models.ForeignKey('Word', on_delete=models.CASCADE)
