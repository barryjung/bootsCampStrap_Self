from django.db import models
from user.models import UserModel
# Create your models here.


class TweetModel(models.Model):
    class Meta:
        db_table = "tweet"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
