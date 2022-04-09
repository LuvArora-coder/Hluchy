
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from audisl import views as aud_view

urlpatterns = [
    path('', include('audisl.urls')),
    path('admin/', admin.site.urls),
    path('save_audio/', aud_view.ajax, name="save_audio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
