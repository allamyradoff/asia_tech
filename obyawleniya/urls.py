from django.urls import path
from .views import *


urlpatterns = [
    path('added_ad_product/', added_ad_product, name="added_ad_product"),

]