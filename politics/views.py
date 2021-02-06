from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.views.generic.detail import DetailView
from politics.google_api_handler import ApiHandler
from politics.propublica_api_handler import ProPub_Api_Handler
from .models import Politician
from django.conf import settings
from datetime import datetime

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

class RepPageView(View):
    template_name = 'myreps.html'

    def get(self, request):
        r = request.user
        today = str(datetime.today().strftime('%Y-%m-%d'))
        existing_rep_list = Politician.objects.filter(constituent=r.username)
        created = " "
        if existing_rep_list.exists():
            created = str(existing_rep_list[0].created_at)

        print("Today: %s" % today)
        print("Created_at: %s" % created)
        
        if existing_rep_list.exists() and created == today:
            print("If executed... pulling from DB")
            return render(request, self.template_name, {'pol_list': existing_rep_list})
        else:
            print("else executed... deleting database entries")
            existing_rep_list.delete()
            print("new api request")
            address = r.address1 + " " + r.city + " " +r.state + " " + r.zip_code
            GoogleHandler = ApiHandler(settings.GOOGLE_URL,address,settings.GOOGLE_API_KEY)
            politician_is = GoogleHandler.create_politician_list(r.username)

            return render(request, self.template_name, {'pol_list': politician_is})

class VoterRegView(TemplateView):
    template_name = 'voterreg.html'

class RepDetailView(DetailView):
    model = Politician
    template_name = 'rep_detail.html'

class UpcomingLegView(View):
    template_name = 'legislation.html'

    def get(self, request):
        house_handler = ProPub_Api_Handler(settings.PRO_PUB_HOUSE)
        senate_handler = ProPub_Api_Handler(settings.PRO_PUB_SENATE)
        house_list = house_handler.call_propub_api()
        senate_list = senate_handler.call_propub_api()

        return render(request, self.template_name, {'house_list': house_list,'senate_list': senate_list})

