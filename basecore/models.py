from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_by=models.CharField(max_length=30,blank=True,editable=False)
    modified_by=models.CharField(max_length=30,blank=True,editable=False)
    created_date=models.DateTimeField(auto_now_add=True,editable=False)
    modified_date=models.DateTimeField(auto_now=True,editable=False)

    class Meta:
        abstract=True


class AddressLine(models.Model):
    address_line1=models.CharField(max_length=30,blank=True)
    address_line2=models.CharField(max_length=50,blank=True)
    city=models.CharField(max_length=50,blank=True)
    postal_code=models.CharField(max_length=6,blank=True)
    phone=models.CharField(max_length=13,blank=True)
    email=models.EmailField(blank=True)

    class Meta:
        abstract=True


