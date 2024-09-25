from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('version/', include('version.urls', namespace='version')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
