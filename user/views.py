from django.shortcuts import render, redirect
from .forms import UserForm, EditProfileForm
from .models import UserModel
from tweet.models import TweetModel


def signup_view(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, 'user/signup.html', {"form": form})
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/user/signup/')


def edit_profile_view(request):
    if request.method == "GET":
        form = EditProfileForm()
        return render(request, 'user/edit_profile.html', {"form": form})
    elif request.method == "POST":
        user = UserModel.objects.get(id=request.user.id)
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.image = form.cleaned_data.get('image')
            user.bio = form.cleaned_data.get('bio')
            user.save()
        return redirect('/')


def follow_view(request, user_id):
    target_user = UserModel.objects.get(id=user_id)
    follow_users = request.user.follow.all()
    if request.user is not target_user:
        if target_user in follow_users:
            request.user.follow.remove(target_user)
        else:
            request.user.follow.add(target_user)
    return redirect('/')


def followpage_view(request):
    follow_users = request.user.follow.all()
    follow_tweets = TweetModel.objects.filter(
        user__in=follow_users).order_by("-created_at")
    return render(request, 'tweet/followpage.html', {"tweets": follow_tweets})
