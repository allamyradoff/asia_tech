from django.contrib import admin
from .models import *

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'order_number', 'first_name', 'phone', 'email', 'state', 'order_total', 'status', 'created_at'
    ]
    inlines = [OrderProductInline]



admin.site.register(Payment)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)