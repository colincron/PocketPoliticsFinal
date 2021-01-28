from django.urls import path
from .views import SignUpView, UserHomePageView, CustomUserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('home/', UserHomePageView.as_view(), name='userhome'),
    path('edit_profile/', CustomUserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success', views.password_success, name="password_success"),
]