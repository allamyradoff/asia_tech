from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.exceptions import ObjectDoesNotExist

from django.http import HttpResponse
from .forms import ReviewForm
from django.contrib import messages
from orders.models import OrderProduct
from banner.models import *
from django.db.models import Count
from accounts.models import UserProfile
from orders.models import OrderProduct
from carts.models import CartItem, Cart
# from carts.views import _cart_id


def home(request):
    product = Product.objects.filter(is_active=True)
    category = Category.objects.all()
    product_sale = Product.objects.filter(is_active=True, is_sale=True)

    top_product = TopProduct.objects.all()
    top_product = top_product[0]
    top_mini_product_all = TopMiniProduct.objects.all()
    top_mini_product = top_mini_product_all[0:2]
    top_mini_product_2 = top_mini_product_all[2:4]
    vip_ad = VipAd.objects.all()
    last_product = Product.objects.all()
    last_product = last_product.order_by('-id')
    last_product = last_product[0:6]

    slider = Slider.objects.all()
    mini_slider = MiniSlider.objects.all()
    logo = Logo.objects.all()

    # if request.user.is_authenticated:
    #     cart_items = CartItem.objects.filter(user=request.user, is_active=True)


    # try:
    #     if request.user.is_authenticated:
    #         cart_items = CartItem.objects.filter(
    #             user=request.user, is_active=True)

    #     else:
    #         cart = Cart.objects.get(cart_id=_cart_id(request))
    #         cart_items = CartItem.objects.filter(cart=cart, is_active=True)

    # except ObjectDoesNotExist:
    #     pass

    




    context = {
        'product': product,
        'category': category,
        'slider': slider,
        'mini_slider': mini_slider,
        'product_sale': product_sale,
        'top_product': top_product,
        'top_mini_product': top_mini_product,
        'top_mini_product_2': top_mini_product_2,
        'vip_ad': vip_ad,
        'last_product': last_product,
        'logo': logo,
        # 'cart_items': cart_items,
    }
    return render(request, 'home.html', context)


def all_product(request):
    all_products = Product.objects.order_by('-id')
    category_count = all_products.count()
    category = Category.objects.all()
    store_banner = StoreBanner.objects.all()
    logo = Logo.objects.all()

    paginator = Paginator(all_products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
    print(paged_products)

    context = {
        'product': paged_products,
        'category': category,
        'category_count': category_count,
        'store_banner': store_banner,
        'logo': logo

    }

    return render(request, 'store.html', context)


def store(request, id):
    category = Category.objects.all()
    product = Product.objects.filter(category=id, is_active=True)
    product = product.order_by('-id')
    all_products = Product.objects.all()
    category_count = all_products.count()
    store_banner = StoreBanner.objects.all()
    logo = Logo.objects.all()

    paginator = Paginator(product, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'product': paged_products,
        'category': category,
        'category_count': category_count,
        'store_banner': store_banner,
        'logo': logo

    }
    return render(request, 'store.html', context)


def product_detail(request, category_id, id):
    product = Product.objects.get(id=id)
    logo = Logo.objects.all()

    if request.user.is_authenticated:

        try:
            orderproduct = OrderProduct.objects.filter(
                user=request.user, product_id=product.id).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = None

    else:
        orderproduct = None

    reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    reviews_count = reviews.count()

    if request.user.is_authenticated:

        profile = UserProfile.objects.filter(user=request.user)
    else:
        profile = None

    context = {
        'product': product,
        'orderproduct': orderproduct,
        'reviews': reviews,
        'profile': profile,
        'reviews_count': reviews_count,
        'logo': logo


    }

    return render(request, 'product_detail.html', context)


def search(request):
    category = Category.objects.all()
    all_products = Product.objects.all()
    category_count = all_products.count()
    store_banner = StoreBanner.objects.all()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product = Product.objects.filter(name__icontains=keyword)
            product_count = product.count()

    context = {
        'product': product,
        'product_count': product_count,
        'category': category,
        'category_count': category_count,
        'store_banner': store_banner,

    }
    return render(request, 'store.html', context)


def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
            review = ReviewRating.objects.get(
                user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=review)
            form.save()
            messages.success(request, "Спасиба за отзыв, Ваш отзый обнавлен")
            return redirect(url)

        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()

                messages.success(request, 'Спасиба за ваш отзый')
                return redirect(url)
