from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('<int:program_id>', views.checkout, name='checkout'),
    path('order_completed/<order_number>', views.order_completed, name='order_completed'),
    path('wh/', webhook, name='webhook'),
]