from django.urls import path
from .views import SignUpView, UserHomePageView, CustomUserEditView, PasswordsChangeView, ConstitutionView, IndependenceView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('home/', UserHomePageView.as_view(), name='userhome'),
    path('edit_profile/', CustomUserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('password_success', views.password_success, name="password_success"),
    path('constitution/', ConstitutionView.as_view(), name='constitution'),
    path('independence/', IndependenceView.as_view(), name='independence')
]