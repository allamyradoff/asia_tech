from django.db import models
from accounts.models import Account

class CategoryAd(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='category_ads/', blank=True, null=True)


    def ad_count(self):
        ac = Ad.objects.filter(cat_id=self.id)
        count = ac.count()
        return count

    def __str__(self):
        return self.name

class Locations(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name="children", on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="locations/", null=True, blank=True)

    def __str__(self):
        return self.title


class Ad(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='ad_test/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='ad_test/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='ad_test/', blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    exchange = models.BooleanField(default=False)
    credit = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    locations = models.ForeignKey(Locations, on_delete=models.CASCADE, blank=True, null=True)
    cat_id = models.ForeignKey(CategoryAd, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f'{self.user.first_name} - {self.name}'



