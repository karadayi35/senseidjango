from django.db import models

class PaymentNotification(models.Model):
    email = models.EmailField()
    txid = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.txid}"