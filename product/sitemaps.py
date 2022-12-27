from django.contrib.sitemaps import Sitemap
from .models import Product

class ProductSitemap(Sitemap):
    changefreq = 'always'
    priority = 0.9

    def items(self):
        return Product.objects.all()