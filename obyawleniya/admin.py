from django.contrib import admin
from .models  import *

class AdsAdmin(admin.ModelAdmin):
    list_display = ('name', 'locations', 'cat_id', 'user')
    list_editable = ('locations',)

admin.site.register(CategoryAd)
admin.site.register(Ad,AdsAdmin)
admin.site.register(Locations)


