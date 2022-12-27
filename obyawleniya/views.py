from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.http import HttpResponse
from banner.models import Logo



def added_ad_product(request):
    cat = CategoryAd.objects.all()
    logo = Logo.objects.all()

    if request.method == 'POST':
        print('ok')
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            form.user = request.user
            form.save()
            return redirect('added_ad_product')
    else:
        form = AdForm()
    return render(request, 'ad/ad-form.html', {'form': form, 'cat':cat, 'logo':logo})



def my_ad(request):
    user = request.user
    ad = Ad.objects.filter(user=user)
    logo = Logo.objects.all()


    context = {
        'ad':ad,
        'logo':logo
    }

    return render(request, 'ad/my_ad_detail.html', context)




def all_ads(request):
    ad = Ad.objects.all()
    ad_count = ad.count()
    cat_ad = CategoryAd.objects.all()


    context = {
        'ad':ad,
        'cat_ad':cat_ad,
        'ad_count':ad_count,
    }

    return render(request, 'ad/ads.html', context)


def ads(request, id):
    ad = Ad.objects.filter(cat_id=id)
    ad_count = ad.count()
    cat_ad = CategoryAd.objects.all()

    context = {
        'ad':ad,
        'cat_ad':cat_ad,
        'ad_count':ad_count,
    }
    return render(request, 'ad/ads.html', context)


def ad_detail(request, id):
    ad = Ad.objects.get(id=id)

    context = {
        'ad':ad,
    }
    return render(request, 'ad/ad_detail.html', context)

