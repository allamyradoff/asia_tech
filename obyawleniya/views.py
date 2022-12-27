from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse
from banner.models import Logo
from carts.models import CartItem, Cart
from carts.views import _cart_id
from obyawleniya.models import CategoryAd



def added_ad_product(request):
    cat = CategoryAd.objects.all()
    logo = Logo.objects.all()
    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            form.user = request.user
            form.save()
            return redirect('added_ad_product')
    else:
        form = AdForm()
    return render(request, 'ad/ad-form.html', {'form': form, 'cat':cat, 'logo':logo, 'cart_items': cart_items, 'ads_cat':ads_cat})



def my_ad(request):
    user = request.user
    ad = Ad.objects.filter(user=user)
    logo = Logo.objects.all()
    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0


    context = {
        'ad':ad,
        'logo':logo,
        'cart_items': cart_items,
        'ads_cat':ads_cat
    }

    return render(request, 'ad/my_ad_detail.html', context)




def all_ads(request):
    ad = Ad.objects.all()
    ad_count = ad.count()
    logo = Logo.objects.all()
    cat_ad = CategoryAd.objects.all()
    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0


    context = {
        'ad':ad,
        'cat_ad':cat_ad,
        'ad_count':ad_count,
        'cart_items': cart_items,
        'ads_cat':ads_cat,
        'logo':logo,

    }

    return render(request, 'ad/ads.html', context)


def ads(request, id):
    ad = Ad.objects.filter(cat_id=id)
    ad_count = ad.count()
    logo = Logo.objects.all()
    cat_ad = CategoryAd.objects.all()
    ads_cat = CategoryAd.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    context = {
        'ad':ad,
        'cat_ad':cat_ad,
        'ad_count':ad_count,
        'cart_items': cart_items,
        'ads_cat':ads_cat,
        'logo':logo,

    }
    return render(request, 'ad/ads.html', context)


def ad_detail(request, id):
    ad = Ad.objects.get(id=id)
    ads_cat = CategoryAd.objects.all()
    logo = Logo.objects.all()


    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    context = {
        'ad':ad,
        'cart_items': cart_items,
        'ads_cat':ads_cat,
        'logo':logo,

    }
    return render(request, 'ad/ad_detail.html', context)

