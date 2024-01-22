from django.db import models


class Client(models.Model):
    id_number = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Account(models.Model):
    account_number = models.CharField(max_length=16, primary_key=True)
    balance = models.FloatField()
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)

class Card(models.Model):
    card_number = models.CharField(max_length=16, primary_key=True)
    owner = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    expiration_date = models.CharField(max_length=5)
    balance = models.FloatField()
# Create your models here.
