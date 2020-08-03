from django.db import models
from datetime import date


# Create your models here



class HWRegister(models.Model):
    id = models.AutoField(primary_key=True)
    hwfname = models.CharField(max_length=50)
    hwlname = models.CharField(max_length=50)
    hwgender = models.CharField(max_length=50, default=True)
    hwdob = models.DateField(default=date.today())
    hwemailid = models.EmailField()
    hwmobileno = models.CharField(max_length=15)
    hwpassword = models.CharField(max_length=64)
    hwaddress = models.TextField()
    hwpincode = models.IntegerField()
    state = models.CharField(max_length=50, default="Null")
    city = models.CharField(max_length=50, default="Null")

    def __str__(self):
        return self.name
class Anganwadi_details(models.Model):
    aw_id                       = models.AutoField(primary_key=True)
    aw_name                     = models.CharField(max_length=500)
    aw_contact1                 = models.CharField(max_length=10, blank=False, null=False, unique=True)
    aw_contact2                 = models.CharField(max_length=10, blank=True, null=True, unique=True)
    aw_address                  = models.CharField(max_length=500)
   
    aw_pincode                  = models.CharField(max_length=6)
    aw_state = models.CharField(max_length=50, default="Null")
    aw_city = models.CharField(max_length=50, default="Null")

    class Meta:
        db_table="anganwadi_details"


    def __str__(self):
        return self.aw_name