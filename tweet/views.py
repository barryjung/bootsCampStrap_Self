from django.shortcuts import render, redirect
from .forms import TweetForm, CommentForm
from .models import TweetModel, CommentModel
# Create your views here.


def feed_view(request):
    tweets = TweetModel.objects.all().order_by('-created_at')
    return render(request, 'tweet/feedpage.html', {"tweets": tweets})


def tweet_create_view(request):
    if request.method == "GET":
        form = TweetForm()
        return render(request, 'tweet/tweet_create.html', {"form": form})
    elif request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
        else:
            form = TweetForm()
            return render(request, 'tweet/tweet_create.html', {"form": form})
        return redirect('/')


def tweet_detail_view(request, tweet_id):
    tweet = TweetModel.objects.get(id=tweet_id)
    comments = tweet.commentmodel_set.all().order_by("-created_at")
    form = CommentForm()
    return render(request, 'tweet/tweet_detail.html', {"tweet": tweet, "comments": comments, "form": form})


def tweet_update_view(request, tweet_id):
    tweet = TweetModel.objects.get(id=tweet_id)
    if request.method == "GET":
        form = TweetForm(instance=tweet)
        return render(request, 'tweet/tweet_update.html', {"form": form})
    elif request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
        else:
            form = TweetForm()
            return render(request, 'tweet/tweet_update.html', {"form": form})
        return redirect('/')


def tweet_delete_view(request, tweet_id):
    tweet = TweetModel.objects.get(id=tweet_id)
    tweet.delete()
    return redirect('/')


def mypage_view(request):
    tweets = TweetModel.objects.filter(
        user=request.user).order_by('-created_at')
    return render(request, 'tweet/mypage.html', {"tweets": tweets})


def like_view(request, tweet_id):
    tweet = TweetModel.objects.get(id=tweet_id)
    if request.user not in tweet.like.all():
        tweet.like.add(request.user)
        return redirect('/')
    else:
        tweet.like.remove(request.user)
        return redirect('/')


def comment_create_view(request, tweet_id):
    tweet = TweetModel.objects.get(id=tweet_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.tweet = tweet
        comment.save()
    return redirect('/tweet/detail/' + str(tweet_id))


def comment_update_view(request, comment_id):
    comment = CommentModel.objects.get(id=comment_id)
    tweet = comment.tweet
    if request.method == "GET":
        form = CommentForm(instance=comment)
        return render(request, 'tweet/tweet_update.html', {"form": form})
    elif request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
        else:
            form = CommentForm(instance=comment)
            return render(request, 'tweet/tweet_update.html', {"form": form})
        return redirect('/tweet/detail/' + str(tweet.id))


def comment_delete_view(request, comment_id):
    comment = CommentModel.objects.get(id=comment_id)
    tweet = comment.tweet
    comment.delete()
    return redirect('/tweet/detail/'+str(tweet.id))
