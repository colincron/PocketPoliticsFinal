from django.db import models

# Create your models here.

class Politician(models.Model):
    name = models.CharField(max_length=50,default="")
    office = models.CharField(max_length=50,default="")
    party = models.CharField(max_length=50,default="", null=True)
    image_url = models.CharField(max_length=200,default="", null=True)
    phone = models.CharField(max_length=13,default="", null=True)
    address_line_1 = models.CharField(max_length=50,default="", null=True)
    city = models.CharField(max_length=30,default="", null=True)
    state = models.CharField(max_length=2,default="", null=True)
    zip_code = models.CharField(max_length=10,default="", null=True)
    facebook = models.CharField(max_length=50,default="", null=True)
    twitter = models.CharField(max_length=50,default="", null=True)
    youtube = models.CharField(max_length=50, default="", null=True)
    id = models.AutoField(primary_key=True)

class Article(models.Model):
    title = models.CharField(max_length=100, default="", null=True)
    author = models.CharField(max_length=50, default="", null=True)
    description = models.TextField(default="",null=True)
    url = models.CharField(max_length=100, default="", null=True)
    url_to_image = models.CharField(max_length=100, default="", null=True)
    id = models.AutoField(primary_key=True)
    
    # def __init__(self, name, office, party, image_url, phone, address_line_1, city, state, zip_code, facebook, twitter, youtube,*args,**kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.name = name
    #     self.office = office
    #     self.party = party
    #     self.image_url = image_url
    #     self.phone = phone
    #     self.address_line_1 = address_line_1
    #     self.city = city 
    #     self.state = state
    #     self.zip_code = zip_code
    #     self.facebook = facebook
    #     self.twitter = twitter
    #     self.youtube = youtube