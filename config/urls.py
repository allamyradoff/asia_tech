
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("product.urls")),
    path('cart/', include("carts.urls")),
    path('accounts/', include("accounts.urls")),
    path('ad/', include("obyawleniya.urls")),

    
    path('orders/', include("orders.urls")),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
