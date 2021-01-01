from django.shortcuts import render
from django.views.generic import TemplateView, View
from politics.api_handler import ApiHandler



# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

class RepPageView(View):
    template_name = 'myreps.html'


    def get(self, request):
        r = request.user
        if r.address2:
            address = r.address1 + " " + r.address2 + " " + r.city + " " +r.state + " " + r.zip_code
        else: 
            address = r.address1 + " " + r.city + " " +r.state + " " + r.zip_code
        GoogleHandler = ApiHandler("https://civicinfo.googleapis.com/civicinfo/v2/representatives?",address,"AIzaSyDprT-PBib6-i5eSdzWxDxVqckzfbyt9DI")
        politician_is = GoogleHandler.create_politician_list()

        
        # return render(request, self.template_name, {'officials': api_response['officials'],'offices': api_response['offices'],'list': indexed_list})
        return render(request, self.template_name, {'pol_list': politician_is})

class VoterRegView(TemplateView):
    template_name = 'voterreg.html'