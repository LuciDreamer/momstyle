from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^', include('momshop.urls')),
    url(r'cart/', include('session_cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)