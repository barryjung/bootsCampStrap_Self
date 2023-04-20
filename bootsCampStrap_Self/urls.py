from django.contrib import admin
from django.urls import path, include
import tweet.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tweet.views.feed_view, name='home'),
    path('user/', include('user.urls')),
    path('tweet/', include('tweet.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
