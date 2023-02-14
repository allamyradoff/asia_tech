from pyexpat import model
from django.db import models
from product.models import *
from obyawleniya.models import CategoryAd

class Slider(models.Model):
    hot_detail = models.CharField(max_length=50, blank=True, null=True)
    link = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    slider_title = models.CharField(max_length=100, blank=True, null=True)
    slider_mini_title = models.CharField(max_length=100, blank=True, null=True)
    slider_image_1 = models.ImageField(
        upload_to="slider_banner/", blank=True, null=True)


    # lilte_banner_1 = models.ImageField(upload_to="litle_banner/", blank=True, null=True)
    # lilte_banner_2 = models.ImageField(upload_to="litle_banner/", blank=True, null=True)
    # big_banner_2 = models.ImageField(upload_to="big_banner/", blank=True, null=True)

    def __str__(self):
        return self.slider_title


class MiniSlider(models.Model):
    mobile_banner = models.ImageField(upload_to='mobile_banner/', blank=True, null=True)
    link_mobile_banner = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    
    lilte_banner_1 = models.ImageField(
        upload_to="litle_banner/", blank=True, null=True)
    lilte_banner_2 = models.ImageField(
        upload_to="litle_banner/", blank=True, null=True)
    slider_title = models.CharField(max_length=100, blank=True, null=True)
    slider_mini_title = models.CharField(max_length=100, blank=True, null=True)
    
    big_banner_2 = models.ImageField(
        upload_to="big_banner/", blank=True, null=True)


    def __str__(self):
        return self.slider_title


class TopProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mini_desc_1 = models.CharField(max_length=50, blank=True, null=True)
    mini_desc_2 = models.CharField(max_length=50, blank=True, null=True)
    mini_desc_3 = models.CharField(max_length=50, blank=True, null=True)
    mini_desc_4 = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.product.name}'


class TopMiniProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.name}'


class VipAd(models.Model):
    title_1 = models.CharField(max_length=50, blank=True, null=True)
    image_1 = models.ImageField(
        upload_to="litle_banner/", blank=True, null=True)
    link = models.ForeignKey(CategoryAd, on_delete=models.PROTECT, blank=True, null=True)
    title_2 = models.CharField(max_length=50, blank=True, null=True)
    image_2 = models.ImageField(
        upload_to="litle_banner/", blank=True, null=True)
    title_3 = models.CharField(max_length=50, blank=True, null=True)
    image_3 = models.ImageField(
        upload_to="litle_banner/", blank=True, null=True)


class StoreBanner(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="store_banner/", blank=True, null=True)

    def __str__(self):
        return self.title


class Cartbanner(models.Model):
    image = models.ImageField(
        upload_to="store_banner/", blank=True, null=True)


class Logo(models.Model):
    image = models.ImageField(
        upload_to="store_banner/", blank=True, null=True)
    image_mobile = models.ImageField(
        upload_to="store_banner/", blank=True, null=True)


class CheckoutBanner(models.Model):
    image = models.ImageField(upload_to="checkout_banner/", blank=True, null=True)

