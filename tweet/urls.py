from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feed_view, name="feed"),
    path('create/', views.tweet_create_view, name="tweet_create"),
    path('detail/<int:id>', views.tweet_detail_view, name="tweet_detail"),
    path('update/<int:id>', views.tweet_update_view, name="tweet_update"),
    path('delete/<int:id>', views.tweet_delete_view, name="tweet_delete"),
]
