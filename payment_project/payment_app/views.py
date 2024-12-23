from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PaymentNotification
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.shortcuts import render
import logging

# Loglama
logger = logging.getLogger(__name__)

class SubmitPaymentView(APIView):
    def post(self, request):
        email = request.data.get('email')
        txid = request.data.get('txid')

        if not email or not txid:
            return Response({"error": "Both email and TXID are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Email doğrulama
        try:
            EmailValidator()(email)
        except ValidationError:
            return Response({"error": "Invalid email address."}, status=status.HTTP_400_BAD_REQUEST)

        # TXID uzunluk kontrolü
        if len(txid) < 10:
            return Response({"error": "TXID is too short."}, status=status.HTTP_400_BAD_REQUEST)

        # Veritabanına kaydetme işlemi
        try:
            PaymentNotification.objects.create(email=email, txid=txid)
            logger.info(f"Payment notification saved for email: {email}")
            return Response({"message": "Payment Notification Saved!"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Error saving payment notification: {str(e)}")
            return Response({"error": "An error occurred while saving the notification."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# CSRF Token görünümü
def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})


# Ana Sayfa Görünümü
def home(request):
    return render(request, 'payment_app/home.html')
