from django.contrib import admin
from .models import TweetModel, CommentModel


class TweetModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'image',
                    'short_content', 'updated_at', 'created_at']
    list_filter = ['user', 'updated_at', 'created_at']


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'tweet', 'user',
                    'short_content', 'updated_at', 'created_at']
    list_filter = ['tweet', 'updated_at', 'created_at']


admin.site.register(TweetModel, TweetModelAdmin)
admin.site.register(CommentModel, CommentModelAdmin)
