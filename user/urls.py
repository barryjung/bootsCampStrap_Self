from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', LoginView.as_view(template_name="user/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
