from django.contrib import admin
from . models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')



class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'price', 'stock', 'created_date', 'is_active', 'is_sale', 'category', 'cource_price')
    list_editable = ('cource_price',)


class VariationAdmin(admin.ModelAdmin):

    list_display = ( 'variation_value', 'variation_category', 'created_date', 'is_active', )
    list_editable = ('is_active',)
    list_filter = ( 'variation_value', 'variation_category',)



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(Cours)


