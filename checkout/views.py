from django.http.response import JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_POST

from programs.models import Program
from .models import Order

from .forms import OrderForm

from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import stripe

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Payment did not go theough!')
        return HttpResponse(content=e, status=400)


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

    if request.method == 'POST':

        profile = UserProfile.objects.get(user=request.user)
        orders = Order.objects.filter(
            program_id=program_id, user_profile=profile, status="paid")
        if orders.count() > 0:
            return JsonResponse({'msg': 'Program already purchased'}, status=400)

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            program_id = Program.objects.get(id=program_id)
            order.program_id = program_id
            profile = UserProfile.objects.get(user=request.user)
            order.user_profile = profile
            order.total_amount = total
            order.save()

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('order_completed', args=[order.order_number]))
        else:
            messages.error(request, 'Something went wrong, please check your information and try again')
   
    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'program': program,
        'total': total,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def order_completed(request, order_number):
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, 'You successfully completed your order')

    template = 'checkout/order_completed.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
