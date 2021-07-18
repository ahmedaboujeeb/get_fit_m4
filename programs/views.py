from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Program
from checkout.models import Order
from profiles.models import UserProfile
from .forms import ProgramForm


@login_required
def all_programs(request):
    # Display programs
    programs = Program.objects.all()
    profile = UserProfile.objects.get(user=request.user)
    orders = Order.objects.filter(user_profile=profile, status="paid")
    res = []

    for prm in programs:
        current_prm = {
            "id": prm.id,
            "name": prm.name,
            "image": prm.image,
            "insight": prm.insight,
            "description": prm.description,
            "sku": prm.sku,
            "paid": False
        }
        for order in orders:
            if prm.id == order.program_id.id:
                current_prm["paid"] = True
                break
        res.append(current_prm)

    context = {
        'programs': res, 
    }

    return render(request, 'programs/programs.html', context)


@login_required
def program_info(request, program_id):
    #Check if program is purchased by user and show program details
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
    # Display user purchased programs
    programs = Program.objects.all()
    profile = UserProfile.objects.get(user=request.user)
    orders = Order.objects.filter(user_profile=profile, status="paid")

    context = {
        'programs': programs,
        'orders': orders,
    }

    return render(request, 'programs/my_programs.html', context)


@login_required
def add_program(request):
    # Make sure it is superuser, add program
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access for to complete this action!')
        return redirect(reverse('programs'))

    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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


@login_required
def edit_program(request, program_id):
    # make sure it is superuser, edit program func
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access for to complete this action!')
        return redirect(reverse('programs'))

    program = get_object_or_404(Program, pk=program_id)
    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES, instance=program)
        if form.is_valid():
            program = form.save()
            messages.success(request, 'Program updated successfully!')
            return redirect(reverse('programs'))
        else:
            messages.error(request, 'Could not update program, please check everything is correct')
    else:
        form = ProgramForm(instance=program)
        messages.info(request, f'You are editting {program.name}')
        
    template = 'programs/edit_program.html'
    context = {
        'form': form,
        'program': program,
    }

    return render(request, template, context)


@login_required
def delete_program(request, program_id):
    # make sure it is super user, delete program functionality
    if not request.user.is_superuser:
        messages.error(request, 'You do not have access for to complete this action!')
        return redirect(reverse('programs'))

    program = get_object_or_404(Program, pk=program_id)
    program.delete()
    messages.success(request, 'Program successfully deleted!')
    return redirect(reverse('programs'))
    