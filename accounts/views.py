from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from politics.news_api_handler import NewsApiHandler
from .voter_registration import url_dict

# Create your views here.

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
        if r.state in url_dict:
            url = url_dict[r.state]
        return render(request, self.template_name, {'news_list': news_list,'voter_url': url})