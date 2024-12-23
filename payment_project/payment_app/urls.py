from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .views import SubmitPaymentView

# CSRF token endpoint view
@csrf_exempt
def get_csrf_token(request):
    return JsonResponse({'csrfToken': ''})

urlpatterns = [
    path('submit-payment/', SubmitPaymentView.as_view(), name='submit-payment'),
    path('get-csrf-token/', get_csrf_token, name='get-csrf-token'),
]
