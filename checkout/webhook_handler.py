from django.http import HttpResponse

from .models import Order

import time

class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'General Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        order_id = intent.metadata.order_id
        
        order_exists = False
        order = None
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    order_number=order_id
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            order.status = "paid"
            order.save()
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            return HttpResponse(
                    content=f'Webhook received: {event["type"]} | Order does not exist',
                    status=500)

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Failed Webhook received: {event["type"]}',
            status=200)