from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Program
from checkout.models import Order
from profiles.models import UserProfile
from .forms import ProgramForm


@login_required
def all_programs(request):

    programs = Program.objects.all()

    context = {
        'programs': programs, 
    }

    return render(request, 'programs/programs.html', context)


@login_required
def program_info(request, program_id):
    #Check if program is purchased by user
    profile = UserProfile.objects.get(user=request.user)
    orders = Order.objects.filter(program_id=program_id, user_profile=profile)
    if orders.count() == 0:
        messages.error(request, 'You have not bought this program')
        return redirect(reverse('programs'))
    else:
        order = orders.first()
        if order.status == 'paid':
            program = Program.objects.get(pk=program_id)
            context = {
                'program': program
            }
            return render(request, 'programs/program_info.html', context)


@login_required
def my_programs(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    orders = profile.orders.all()

    context = {
        'orders': orders,
    }

    return render(request, 'programs/my_programs.html', context)


@login_required
def add_program(request):
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access for to complete this action!')
        return redirect(reverse('programs'))

    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            program = form.save()
            messages.success(request, 'Program added successfully!')
            return redirect(reverse('programs'))
        else:
            messages.error(request, 'Could not add program, please check everything is correct')
    else:
        form = ProgramForm()
        
    template = 'programs/add_program.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
