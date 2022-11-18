from django.urls import path
from .views import *


urlpatterns = [
    path('added_ad_product/', added_ad_product, name="added_ad_product"),
    path('my_ad/', my_ad, name="my_ad"),
    path('all_ads/', all_ads, name="all_ads"),
    path('ad_detail/<int:id>/', ad_detail, name="ad_detail"),

]