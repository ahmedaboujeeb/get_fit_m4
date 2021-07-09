from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_programs, name='programs'),
    path('<int:program_id>/', views.program_info, name='program_info'),
    path('my_programs/', views.my_programs, name='my_programs'),
    path('add/', views.add_program, name='add_program'),
]