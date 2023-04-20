from django.shortcuts import render, redirect
from .forms import UserForm, EditProfileForm


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
        form = EditProfileForm(instance=request.user)
        return render(request, 'user/edit_profile.html', {"form": form})
    elif request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return redirect('/')
