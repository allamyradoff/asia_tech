from django.db import models
from accounts.models import Account
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    desc = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='category/', blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def prod_count(self):
        pc = Product.objects.filter(category=self.id)
        count = pc.count()
        return count

    def __str__(self):
        return self.name


class Cours(models.Model):
    cours = models.FloatField()


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    desc = models.TextField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    image_1 = models.ImageField(upload_to='products/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    is_sale = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    sale_percent = models.CharField(max_length=10, blank=True, null=True)
    sale_price = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cource_price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_price(self):
        course = Cours.objects.latest('id')
        price = self.price * course.cours
        return price

    def save(self, *args, **kwargs):
        course = Cours.objects.latest('id')
        price = self.price * course.cours
        self.cource_price = price

        super(Product, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.category.id])


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category="color", is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category="size", is_active=True)


variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)


class Variation(models.Model):
    product = models.ManyToManyField(Product)
    variation_category = models.CharField(
        max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value


class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
