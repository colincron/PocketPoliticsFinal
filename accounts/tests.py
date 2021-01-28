from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from .models import StandardUser
from .views import UserHomePageView
import datetime
# Create your tests here.

class SignupPageTests(TestCase):
    is_superuser = False
    first_name = 'test'
    last_name = 'user'
    username = 'test_user'
    email = 'testuser@test.com'
    password = '!QAZ2wsx#EDC4rfv'
    address1 = '8044 25th Ave N'
    address2 = None
    city = 'Saint Petersburg'
    state = 'FL'
    zip_code = '33710'
    dob = '1989-09-10'
    pol_preference = 'green_party'
    groups = "test_group"
    user_permissions = "nfc"
    is_active = True
    is_staff = False

    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        new_user = StandardUser(
            is_superuser=False, 
            password="!QAZ2wsx#EDC4rfv", 
            username=self.username,
            email=self.email,
            is_active=self.is_active,
            first_name=self.first_name, 
            last_name=self.last_name,
            is_staff=self.is_staff,  
            address1=self.address1, 
            address2=self.address2, 
            city=self.city, 
            state=self.state, 
            zip_code=self.zip_code, 
            dob=self.dob, 
            pol_preference=self.pol_preference
        )
        new_user.save()
        self.assertEqual(StandardUser.objects.all().count(),1)
        self.assertEqual(StandardUser.objects.first().is_superuser, False)
        self.assertEqual(StandardUser.objects.first().password, '!QAZ2wsx#EDC4rfv')
        self.assertEqual(StandardUser.objects.first().username, 'test_user')
        self.assertEqual(StandardUser.objects.first().email, 'testuser@test.com')
        self.assertEqual(StandardUser.objects.first().is_active, True)
        self.assertEqual(StandardUser.objects.first().first_name, 'test')
        self.assertEqual(StandardUser.objects.first().last_name, 'user')
        self.assertEqual(StandardUser.objects.first().is_staff, False)
        self.assertEqual(StandardUser.objects.first().address1, '8044 25th Ave N')
        self.assertEqual(StandardUser.objects.first().address2, None)
        self.assertEqual(StandardUser.objects.first().city, 'Saint Petersburg')
        self.assertEqual(StandardUser.objects.first().state, 'FL')
        self.assertEqual(StandardUser.objects.first().zip_code, '33710')
        self.assertEqual(StandardUser.objects.first().dob, datetime.date(1989,9,10))
        self.assertEqual(StandardUser.objects.first().pol_preference, 'green_party')


class UserHomePageTests(TestCase):
    is_superuser = False
    first_name = 'test'
    last_name = 'user'
    username = 'test_user'
    email = 'testuser@test.com'
    password = '!QAZ2wsx#EDC4rfv'
    address1 = '8044 25th Ave N'
    address2 = None
    city = 'Saint Petersburg'
    state = 'FL'
    zip_code = '33710'
    dob = '1989-09-10'
    pol_preference = 'green_party'
    is_active = True
    is_staff = False

    def create_user(self):
        new_user = StandardUser(
                is_superuser=False, 
                password="!QAZ2wsx#EDC4rfv", 
                username=self.username,
                email=self.email,
                is_active=self.is_active,
                first_name=self.first_name, 
                last_name=self.last_name,
                is_staff=self.is_staff,  
                address1=self.address1, 
                address2=self.address2, 
                city=self.city, 
                state=self.state, 
                zip_code=self.zip_code, 
                dob=self.dob, 
                pol_preference=self.pol_preference
            )
        new_user.save()
        return new_user

    def test_user_home_status_code(self):
        self.create_user()
        client = Client(username="test_user",password="!QAZ2wsx#EDC4rfv")
        response = client.get('/accounts/home/')
        self.assertEqual(response.status_code, 200)
        
        