from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date', 'user_profile',
                       'total_amount', 'status', 'stripe_pid',)

    fields = ('order_number', 'date', 'user_profile', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county','total_amount',
              'status', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'total_amount', 'status',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)