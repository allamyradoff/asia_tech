from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse
from banner.models import Logo
from carts.models import CartItem, Cart
from carts.views import _cart_id
from obyawleniya.models import CategoryAd
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from banner.models import StoreBanner
from product.models import Category
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def added_ad_product(request):
    cat = CategoryAd.objects.all()
    logo = Logo.objects.all()
    ads_cat = CategoryAd.objects.all()
    category = Category.objects.all()
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0
    try: 
        if request.method == 'POST':
            form = AdForm(request.POST, request.FILES)
            if form.is_valid():
                form = form.save()
                form.user = request.user
                form.save()
                return redirect('my_ad')
        else:
            form = AdForm()
    except:
        return HttpResponse('suraty girizmegiňizi haýyş edýäris')
        
    return render(request, 'ad/ad-form.html', {'form': form, 'cat':cat, 'logo':logo, 'cart_items': cart_items, 'ads_cat':ads_cat, 'category':category})



def my_ad(request):
    user = request.user
    ad = Ad.objects.filter(user=user)
    logo = Logo.objects.all()
    ads_cat = CategoryAd.objects.all()
    category = Category.objects.all()
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    context = {
        'ad':ad,
        'logo':logo,
        'cart_items': cart_items,
        'ads_cat':ads_cat,
        'category':category
    }

    return render(request, 'ad/my_ad_detail.html', context)


def edit_ad(request, id):    
    ad = Ad.objects.get(id=id)
    category = Category.objects.all()

    if request.method == "POST":
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return HttpResponse('OK')

    context = {
        'ad':ad,
        'form':AdForm(instance=ad),
        'category':category
    }


    return render(request, 'ad/edit_ad.html', context)



def all_ads(request):
    ad = Ad.objects.all().order_by('-created_at')
    ad_all = Ad.objects.all()
    ad_count_all = ad_all.count()
    ad_count = ad.count()
    logo = Logo.objects.all()
    cat_ad = CategoryAd.objects.all()
    ads_cat = CategoryAd.objects.all()
    store_banner = StoreBanner.objects.all()
    locations = Locations.objects.all()
    category = Category.objects.all()

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    LocationID = request.GET.get('loactionID')

    if LocationID:
        ad = Ad.objects.filter(locations=LocationID).order_by('-created_at')
    else:
        ad = Ad.objects.all().order_by('-created_at')

    paginator = Paginator(ad, 8)
    page = request.GET.get('page')
    paged_ads = paginator.get_page(page)

    context = {
        'ad':paged_ads,
        'cat_ad':cat_ad,
        'ad_count':ad_count,
        'cart_items': cart_items,
        'ads_cat':ads_cat,
        'logo':logo,
        'locations':locations,
        'ad_count_all':ad_count_all,
        'store_banner':store_banner,
        'category':category,
        'ad_count':ad_count,
    }

    return render(request, 'ad/ads.html', context)


def ads(request, id):
    ad_all = Ad.objects.all().order_by('-created_at')
    ad_count_all = ad_all.count()
    category = Category.objects.all()
    ad = Ad.objects.filter(cat_id=id)
    print()
    ad_count = ad.count()
    logo = Logo.objects.all()
    cat_ad = CategoryAd.objects.all()
    ads_cat = CategoryAd.objects.all()
    store_banner = StoreBanner.objects.all()
    ad_locations = Ad.objects.filter(cat_id=id)
    locations = Locations.objects.all()
    LocationID = request.GET.get('loactionID')

    if LocationID:
        ad = Ad.objects.filter(locations=LocationID).order_by('-created_at')
        ad = ad.filter(cat_id=id)
    else:
        ad = Ad.objects.filter(cat_id=id).order_by('-created_at')

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0
    ad_counts = ad.count()

    current_id = id
    location_id = LocationID

    context = {
        'ad':ad,
        'cat_ad':cat_ad,
        'ad_count':ad_count,
        'cart_items': cart_items,
        'ads_cat':ads_cat,
        'logo':logo,
        'locations':locations,
        'ad_count_all':ad_count_all,
        'store_banner':store_banner,
        'ad_counts':ad_counts,
        "current_id": current_id,
        "location_id":location_id,
        'category':category
    }
    return render(request, 'ad/ads.html', context)


def ad_detail(request, id):
    ad = Ad.objects.get(id=id)
    ad.seen_count = ad.seen_count + 1
    ad.save()
    ads_cat = CategoryAd.objects.all()
    logo = Logo.objects.all()
    category = Category.objects.all()




    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user, is_active=True)
    else:
        cart_items = 0

    context = {
        'ad':ad,
        'cart_items': cart_items,
        'ads_cat':ads_cat,
        'logo':logo,
        'category':category
    }
    return render(request, 'ad/ad_detail.html', context)


def delete_ad(request, id):
    ad = Ad.objects.get(id=id)
    ad.delete()
    return redirect(my_ad)

