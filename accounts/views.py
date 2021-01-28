from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserEditForm
from politics.news_api_handler import NewsApiHandler
from .voter_registration import url_dict
from politics.reddit_api_handler import RedditApiHandler
from django.views.generic.edit import UpdateView
from django.conf import settings


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserHomePageView(TemplateView):
    template_name = 'userhome.html'

    def get(self,request):
        NewsHandler = NewsApiHandler("url")
        news_list = NewsHandler.call_news_api()
        r = request.user
        url = ""
        RedditHandler = RedditApiHandler(settings.REDDIT_API_URL)
        reddit_list = RedditHandler.call_reddit_api()
        if r.state in url_dict:
            url = url_dict[r.state]
        
        return render(request, self.template_name, {'news_list': news_list,'reddit_list': reddit_list, 'voter_url': url})


class CustomUserEditView(UpdateView):
    form_class = CustomUserEditForm
    success_url = reverse_lazy('userhome')
    template_name = 'registration/edit_profile.html'

    def get_object(self):
        return self.request.user 

def CustomPageNotFoundView(request,exception):
    return render(template_name="custom_404.html")