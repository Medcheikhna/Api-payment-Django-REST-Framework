# views.py
# views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Client, Account, Card
from .serializers import ClientSerializer, AccountSerializer, CardSerializer
from django.views.decorators.csrf import csrf_exempt
import json
from django.forms.models import model_to_dict

@csrf_exempt
@api_view(['POST'])
def create_client(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        try:
            new_client = Client.objects.create(**data)
            serialized_client = model_to_dict(new_client)
            return JsonResponse({'message': 'Client created successfully', 'client': serialized_client})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@api_view(['POST'])
def create_account(request):
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Account created successfully', 'account': serializer.data})
        return Response({'error': serializer.errors}, status=400)

@csrf_exempt
@api_view(['POST'])
def create_card(request):
    if request.method == 'POST':
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Card created successfully', 'card': serializer.data})
        return Response({'error': serializer.errors}, status=400)

@csrf_exempt
@api_view(['GET'])
def get_account_balance(request, account_number):
    account = get_object_or_404(Account, account_number=account_number)
    serialized_account = model_to_dict(account)
    return JsonResponse({'account': serialized_account})

@csrf_exempt
@api_view(['GET'])
def get_card_balance(request, card_number):
    card = get_object_or_404(Card, card_number=card_number)
    serialized_card = model_to_dict(card)
    return JsonResponse({'card': serialized_card})

# ... (other functions remain the same)


@csrf_exempt
@api_view(['POST'])
def deposit_to_card(request):
    if request.method == 'POST':
        data = request.data
        card_number = data.get('card_number')
        deposited_amount = data.get('deposited_amount')

        if not card_number or deposited_amount is None:
            return JsonResponse({'error': 'Card number and deposited amount are required'}, status=400)

        card = get_object_or_404(Card, card_number=card_number)

        if deposited_amount <= 0:
            return JsonResponse({'error': 'Invalid deposit amount'}, status=400)

        card.balance += deposited_amount
        card.save()

        serialized_card = model_to_dict(card)
        return JsonResponse({'message': 'Deposit successful', 'card': serialized_card})
@csrf_exempt
@api_view(['POST'])
def make_payment(request):
    if request.method == 'POST':
        data = request.data
        card_number = data.get('card_number')
        owner = data.get('owner')
        cvv = data.get('cvv')
        expiration_date = data.get('expiration_date')
        account_number = data.get('account_number')
        amount = data.get('amount')

        if not card_number or not owner or not cvv or not expiration_date or not account_number or amount is None:
            return JsonResponse({'error': 'Incomplete payment data'}, status=400)

        card = get_object_or_404(Card, card_number=card_number)

        if card.owner != owner or card.cvv != cvv or card.expiration_date != expiration_date:
            return JsonResponse({'error': 'Card details do not match'}, status=400)

        account = get_object_or_404(Account, account_number=account_number)

        if card.balance < amount:
            return JsonResponse({'error': 'Insufficient balance on card'}, status=400)

        card.balance -= amount
        account.balance += amount

        card.save()
        account.save()

        serialized_card = CardSerializer(card).data
        serialized_account = AccountSerializer(account).data
        return JsonResponse({'message': 'Payment successful', 'card': serialized_card, 'account': serialized_account})