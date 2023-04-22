from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.tweet_create_view, name="tweet_create"),
    path('detail/<int:tweet_id>', views.tweet_detail_view, name="tweet_detail"),
    path('update/<int:tweet_id>', views.tweet_update_view, name="tweet_update"),
    path('delete/<int:tweet_id>', views.tweet_delete_view, name="tweet_delete"),
    path('mypage/', views.mypage_view, name="mypage"),
    path('like/<int:tweet_id>', views.like_view, name="like"),
    path('comment/create/<int:tweet_id>',
         views.comment_create_view, name="comment_create"),
    path('comment/update/<int:comment_id>',
         views.comment_update_view, name="comment_update"),
    path('comment/delete/<int:comment_id>',
         views.comment_delete_view, name="comment_delete"),
]
