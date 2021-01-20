from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from politics.google_api_handler import ApiHandler

# Create your models here.

party_choices = (
    ('democratic_party', 'Democratic Party'),
    ('green_party', 'Green Party'),
    ('libertarian_party', 'Libertarian Party'),
    ('republican_party', 'Republican Party'),
    ('vermont_progressive', 'Vermont Progressive Party'),
    ('alliance_party', 'Alliance Party'),
    ('popular_democratic_party', "Popular Democratic Party"),
    ('new_progressive','New Progressive Party'),
    ('citizens_victory_movement', "Citizen's Victory Movement"),
    ('puerto_rican_independence', 'Puerto Rican Independence Party'),
)

class StandardUser(AbstractUser):
    address1 = models.CharField( max_length=50 )
    address2 = models.CharField( max_length=50, blank=True )
    city = models.CharField( max_length=25 )
    state = models.CharField( max_length=2 )
    zip_code = models.CharField( max_length=5 )
    dob = models.DateField(blank=True, null=True)
    pol_preference = models.CharField(max_length=30, choices=party_choices, default='')