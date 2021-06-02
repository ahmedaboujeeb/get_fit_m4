from django.shortcuts import get_object_or_404, render
from .models import Program


def all_programs(request):

    programs = Program.objects.all()

    context = {
        'programs': programs, 
    }

    return render(request, 'programs/programs.html', context)


def program_info(request, program_id):

    program = get_object_or_404(Program, pk=program_id)

    context = {
        'program': program, 
    }

    return render(request, 'programs/program_info.html', context)