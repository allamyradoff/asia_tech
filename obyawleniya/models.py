from django.db import models
from accounts.models import Account

class CategoryAd(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='ad/', blank=True, null=True)
    exchange = models.BooleanField(default=False)
    credit = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    

    cat_id = models.ForeignKey(CategoryAd, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return f'{self.user.first_name} - {self.name}'