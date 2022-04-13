
from django.db import models
from django.db.models.enums import Choices
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
class Pet(models.Model):
    STATES = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
    
    PET_STATUS = (
        ('adopted','adopted'),
        ('not_adopted','not_adopted')
    )
    
    PET_GENDER = (
        ('male','male'),
        ('female','female')
    )
    PET_CATEGORY = (
        ('Dog','Dog'),
        ('Cat','Cat'),
        ('Rabbit','Rabbit'),
    )
    PET_AGE = (
        ('Upto 6 months','Upto 6 months'),
        ('6-8 months','6-8 months'),
        ('1.5-3 years','1.5-3 years'),
        ('3 years or more','3 years or more'),
    )
    PET_YES_OR_NO = (
        ('Yes','Yes'),
        ('No','No'),
    )
    pet_category            = models.CharField(max_length=50,choices=PET_CATEGORY)
    pet_name                = models.CharField(max_length=10)
    pet_age                 = models.CharField(max_length=50,choices=PET_AGE)
    pet_bread               = models.CharField(max_length=60)
    pet_gender              = models.CharField(max_length=10,choices = PET_GENDER)
    pet_image               = models.ImageField(upload_to = 'Pet_pic',default="", null=True, blank=True)
    pet_vaccinated          = models.CharField(max_length=3,choices=PET_YES_OR_NO,default="")
    pet_neutered            = models.CharField(max_length=3,choices=PET_YES_OR_NO,default="")
    pet_sprayed             = models.CharField( max_length=3,choices=PET_YES_OR_NO,default="")
    pet_good_kids           = models.CharField( max_length=3,choices=PET_YES_OR_NO,default="")
    pet_address             = models.CharField (max_length=60,choices=STATES,default="")
    pet_good_pets           = models.CharField(max_length=3,choices=PET_YES_OR_NO,default="")
    pet_desc                = models.CharField(max_length=1000, default="")
    pet_status              = models.CharField(max_length=40,choices=PET_STATUS,default="not_adopted")
    pet_owner               = models.ForeignKey(User, on_delete=models.CASCADE , default = "")
    pet_interest            = models.IntegerField(default = 0)
    pet_not_interest        = models.IntegerField(default = 0)
    
    

    def __str__(self):
        return f"{self.pet_category}-{self.pet_name}"

    def get_absolute_url(self):
        print('check')
        return reverse('pet_profile', kwargs={"pk": self.pk})
    
    # def save(self,*args, **kwargs):
    #     super(Pet,self).save(  *args, **kwargs)

    #     img = Image.open(Pet.pet_image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.pet_image.path)