from django.shortcuts import render, redirect
from .forms import TweetForm
from .models import TweetModel
# Create your views here.


def feed_view(request):
    tweets = TweetModel.objects.all().order_by('-created_at')
    return render(request, 'tweet/feedpage.html', {"tweets": tweets})


def tweet_create_view(request):
    if request.method == "GET":
        form = TweetForm()
        return render(request, 'tweet/tweet_create.html', {"form": form})
    elif request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
        else:
            form = TweetForm()
            return render(request, 'tweet/tweet_create.html', {"form": form})
        return redirect('/')
