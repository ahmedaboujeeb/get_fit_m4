from checkout.forms import OrderForm
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib import messages

from programs.models import Program
from checkout.models import Order

from .forms import OrderForm

import stripe


def checkout(request, program_id):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    program = get_object_or_404(Program, pk=program_id)

    total = program.price
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'program': program,
        'total': total,
        'stripe_public_key': 'stripe_public_key',
        'client_secret': 'stripe_secret_key',
    }

    return render(request, template, context)
