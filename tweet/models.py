from django.db import models
from user.models import UserModel
# Create your models here.


class TweetModel(models.Model):
    class Meta:
        db_table = "tweet"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="tweet_image/%y/%m/%d", blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(
        UserModel, blank=True, related_name="like_user")


class CommentModel(models.Model):
    class Meta:
        db_table = "comment"

    tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
