from django.shortcuts import render, redirect
from .forms import UserForm

# Create your views here.


def signup_view(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, 'user/signup.html', {"form": form})
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/user/signup/')
