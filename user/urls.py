from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', LoginView.as_view(template_name="formpage.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('edit/', views.edit_profile_view, name="edit_profile"),
    path('follow/<int:user_id>', views.follow_view, name="follow"),
    path('followpage/', views.followpage_view, name="followpage"),
]
