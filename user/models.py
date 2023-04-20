from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    class Meta:
        db_table = "user"

    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to="user_images", blank=True,
                              default="/static/image/150.png")
