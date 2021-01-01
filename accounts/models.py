from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

party_choices = (
    ('democratic_party', 'Democratic Party'),
    ('green_party', 'Green Party'),
    ('libertarian_party', 'Libertarian Party'),
    ('republican_party', 'Republican Party'),
)

class StandardUser(AbstractUser):
    address1 = models.CharField( max_length=50 )
    address2 = models.CharField( max_length=50, blank=True )
    city = models.CharField( max_length=25 )
    state = models.CharField( max_length=2 )
    zip_code = models.CharField( max_length=5 )
    dob = models.DateField(blank=True, null=True)
    pol_preference = models.CharField(max_length=30, choices=party_choices, default='')