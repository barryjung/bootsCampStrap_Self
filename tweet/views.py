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


def tweet_detail_view(request, id):
    tweet = TweetModel.objects.get(id=id)
    return render(request, 'tweet/tweet_detail.html', {"tweet": tweet})


def tweet_update_view(request, id):
    tweet = TweetModel.objects.get(id=id)
    if request.method == "GET":
        form = TweetForm(instance=tweet)
        return render(request, 'tweet/tweet_update.html', {"form": form})
    elif request.method == "POST":
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid():
            form.save()
        else:
            form = TweetForm()
            return render(request, 'tweet/tweet_update.html', {"form": form})
        return redirect('/')


def tweet_delete_view(request, id):
    tweet = TweetModel.objects.get(id=id)
    tweet.delete()
    return redirect('/')
