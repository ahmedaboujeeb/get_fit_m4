from django.urls import path
from . import views

urlpatterns = [
    path('<int:program_id>', views.checkout, name='checkout')
]