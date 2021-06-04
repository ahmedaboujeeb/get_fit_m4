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
        'stripe_public_key': 'pk_test_51IpsIQIHH9h4Wbq5E3eRjo6XfyXRqLLOj0iYIwqd4K3bUgfpTLPIgEFkhNQCxP5wxTDh8yhh9E3fmyA3XRaQ4Sze00WwH9Doxa',
        'client_secret': 'sk_test_51IpsIQIHH9h4Wbq5TMJSoJ3Epw5Nkxw1GgrQZShMf5aqQeZuCP1p81tGZEtOff5NBfZfOZM5Zsdt3RNx1kWPQnGK005fsKdYUK',
    }

    return render(request, template, context)
