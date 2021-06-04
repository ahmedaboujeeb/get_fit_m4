from checkout.forms import OrderForm
from django.shortcuts import render, get_object_or_404

from programs.models import Program
from checkout.models import Order

from .forms import OrderForm


def checkout(request, program_id):

    program = get_object_or_404(Program, pk=program_id)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'program': program,
    }

    return render(request, template, context)
