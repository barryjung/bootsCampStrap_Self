from django.shortcuts import render, redirect
from .forms import UserForm, EditProfileForm
from .models import UserModel


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
