# payment_app/forms.py
from django import forms
from .models import PaymentNotification

class PaymentNotificationForm(forms.ModelForm):
    class Meta:
        model = PaymentNotification
        fields = ['email', 'txid']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'txid': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter TXID'}),
        }
