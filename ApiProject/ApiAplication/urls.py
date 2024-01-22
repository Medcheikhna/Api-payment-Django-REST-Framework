# Django URL patterns (urls.py)

from django.http import HttpResponse
from django.urls import path
from .views import create_client, create_account, get_account_balance, create_card, get_card_balance, deposit_to_card, make_payment

urlpatterns = [
    path('create_client/',create_client),
    path('create_account/',create_account),
    path('account_balance/<str:account_number>/',get_account_balance),
    path('create_card/',create_card),
    path('card_balance/<str:card_number>/',get_card_balance),
    path('deposit_to_card/',deposit_to_card),
    path('make_payment/',make_payment),
    # path('', lambda request: HttpResponse("Welcome to the ApiAplication app")),
]
