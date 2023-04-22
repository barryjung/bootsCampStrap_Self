from django.db import models
from user.models import UserModel
from django.conf import settings
import os


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

    @property
    def short_content(self):
        return self.content[:15]

    def __str__(self):
        return self.short_content

    def save(self):
        if self.id is not None:
            oldimage = self.__class__.objects.get(id=self.id).image
            if oldimage and oldimage != self.image:
                os.remove(oldimage.path)
        super().save()

    def delete(self):
        if self.image:
            os.remove(self.image.path)
        super().delete()


class CommentModel(models.Model):
    class Meta:
        db_table = "comment"

    tweet = models.ForeignKey(TweetModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def short_content(self):
        return self.content[:15]

    def __str__(self):
        return self.short_content
