from django.contrib import admin
from django.urls import path, include
import tweet.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tweet.views.feed_view, name='home'),
    path('user/', include('user.urls')),
    path('tweet/', include('tweet.urls')),
]
