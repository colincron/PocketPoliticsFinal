from django.urls import path
from .views import HomePageView, RepPageView, VoterRegView, RepDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('myreps/', RepPageView.as_view(), name='myreps'),
    path('voterregistration/', VoterRegView.as_view(), name='voterreg'),
    path('myreps/<int:pk>/', RepDetailView.as_view(), name='repdetail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)