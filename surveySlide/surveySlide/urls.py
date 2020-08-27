from django.contrib import admin
from django.urls import path, include
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    
    path('account/', include('django.contrib.auth.urls')),    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
