from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from politics.news_api_handler import NewsApiHandler

# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class UserHomePageView(TemplateView):
    template_name = 'userhome.html'

    def get(self,request):
        foo = NewsApiHandler("url")
        news_list = foo.call_news_api()
        return render(request, self.template_name, {'news_list': news_list})