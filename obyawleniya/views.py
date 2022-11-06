from django.shortcuts import render, redirect
from .forms import *
from .models import *





def added_ad_product(request):
    cat = CategoryAd.objects.all()

    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES)
        if form.is_valid():
            # user = request.user
            # name = form.cleaned_data['name']
            # desc = form.cleaned_data['desc']
            # image = form.cleaned_data['image']
            # cat_id = form.cleaned_data['cat_id']
            # form = Ad.objects.create(
            #     user=user,
            # )
            form = form.save()
            form.user = request.user
            form.save()
            return redirect('added_ad_product')
    else:
        form = AdForm()
    return render(request, 'ad/ad-form.html', {
        'form': form, 'cat':cat
    })

