from django.urls import path
from .views import SignUpView, UserHomePageView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('home/', UserHomePageView.as_view(), name='userhome'),
]