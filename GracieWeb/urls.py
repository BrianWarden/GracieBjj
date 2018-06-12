from django.contrib import admin
from django.urls import path, include
from videos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('watch/<int:video_id>', views.watch, name='watch'),
    path('library/', views.library, name="library"),
    path('accounts/', include('accounts.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
