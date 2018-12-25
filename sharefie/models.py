from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import  User
from django.core.files.storage import FileSystemStorage

def upload_location(instance,filename):
    return "%s/%s"%(str(instance.mobile_number),filename)

#regesiter mobile number table
class UserDetails(models.Model):
    full_name = models.CharField(max_length=100, null= True, blank=True)
    mobile_number = models.BigIntegerField(unique=True)
    email_id = models.EmailField(null=True,blank=True)
    otp = models.CharField(max_length=50,null=True,blank=True)
    otp_verify = models.BooleanField(default=False)
    imei_udid = models.CharField(max_length=50,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.NullBooleanField(default=None)
    domain_status = models.NullBooleanField(default=None)

    def __str__(self):
        return str(self.mobile_number)

class Mails(models.Model):
    user_name = models.CharField(max_length=1000 , null=True,blank=True)
    email_id = models.CharField(max_length=1000, null=True, blank=True)
    domain_status = models.NullBooleanField(default=True)

    def __str__(self):
        return str(self.id)

# stroing mails with respective mobilenumbers
class UserMails(models.Model):
    userdetails = models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    mobile_number = models.BigIntegerField(null=True,blank=True)
    mapped_mails = models.ManyToManyField(Mails)

    def __str__(self):
        return str(self.mobile_number)

# used to store files
class ShredFiles(models.Model):
    docu_name = models.CharField(max_length=1000, null=True,blank=True)
    file = models.FileField('file',upload_to=upload_location,\
                            storage=FileSystemStorage(location=settings.MEDIA_ROOT),null=True,blank=True)
    date_time = models.DateTimeField(blank=True,null=True)
    transaction = models.IntegerField(null=True,blank=True)
    mobile_number = models.BigIntegerField()
    file_status = models.BooleanField(default=True)
    userdetails = models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    mail_send = models.BooleanField(default=True)

    def __str__(self):
        return self.docu_name

class Remarks(models.Model):
    mobile_number =models.BigIntegerField()
    remarks = models.TextField(blank=True,null=True)
    transaction = models.IntegerField(default=1)
    remarks_status = models.BooleanField(default=True)
    date_time = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.mobile_number



