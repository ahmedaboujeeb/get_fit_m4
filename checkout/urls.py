from django.urls import path
from . import views

urlpatterns = [
    path('<int:program_id>', views.checkout, name='checkout'),
    path('order_completed/<order_number>', views.order_completed, name='order_completed'),
]