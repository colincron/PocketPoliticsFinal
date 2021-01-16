from django.urls import path
from .views import SignUpView, UserHomePageView, CustomUserEditView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('home/', UserHomePageView.as_view(), name='userhome'),
    path('edit_profile/', CustomUserEditView.as_view(), name='edit_profile'),
]