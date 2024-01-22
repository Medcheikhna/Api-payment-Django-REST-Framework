# serializers.py
from rest_framework import serializers
from .models import Client, Account, Card

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['card_number', 'owner', 'cvv', 'expiration_date', 'balance']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['account_number', 'balance', 'owner']