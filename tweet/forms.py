from django.forms import ModelForm
from .models import TweetModel, CommentModel


class TweetForm(ModelForm):
    class Meta:
        model = TweetModel
        fields = ['image', 'content']


class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['content']
