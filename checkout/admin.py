from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date',
                       'total_amount',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county','total_amount',)

    list_display = ('order_number', 'date', 'full_name',
                    'total_amount',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)