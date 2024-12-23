# payment_app/admin.py
from django.contrib import admin
from .models import PaymentNotification

@admin.register(PaymentNotification)
class PaymentNotificationAdmin(admin.ModelAdmin):
    list_display = ('email', 'txid', 'created_at')
    search_fields = ('email', 'txid')