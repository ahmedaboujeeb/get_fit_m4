from django.shortcuts import render
from .models import Program


def all_programs(request):

    programs = Program.objects.all()

    context = {
        'programs': programs, 
    }

    return render(request, 'programs/programs.html', context)