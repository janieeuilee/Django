from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.utils.text import slugify
# Create your models here.
class ApplyBuffer(models.Model):
    request_date = models.DateTimeField('Request Date', auto_now_add=True)
    indi_id = models.ForeignKey(User, related_name='individual_id', null=False, on_delete=models.CASCADE)
    ent_id = models.ForeignKey(User, related_name='enterprise_id', null=False, on_delete=models.CASCADE)

# class InputForm(models.Model):
#     name_indi                   = models.description('NAME_INDI', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     social_id                   = models.description('SOCIAL_ID', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     address_indi                = models.description('ADDRESS_INDI', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     name_enterprise             = models.description('NAME_ENTERPRISE', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     Business_license_number     = models.description('BUINESS_LICENSE_NUMBER',max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     representative_name         = models.description('REPRESENTATIVE_NAME', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     industry                    = models.description('INDUSTRY', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     address_ent                 = models.description('ADDRESS_ENT', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     department                  = models.description('DEPARTMENT', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     position                    = models.description('POSITION', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     assigned_task               = models.description('ASSIGNED_TASK', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     content                     = models.TextField('CONTENT')
#     working_period              = models.description('WORKING_PERIOD', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     department_a                = models.description('DEPARTMENT_A', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     name_a                      = models.description('NAME_A', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     position_a                  = models.description('POSITION_A', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     contact_number_a            = models.description('CONTACT_NUMBER_A', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     purpose                     = models.description('PURPOSE', max_length=100, blank=True, null=True, help_text='simple descripton text.')
#     create_date                 = models.DateTimeField('Create Date', auto_now_add=True)

#     def get_absolute_url(self): 
        # return reverse('mysite:data_app', args=[self.id])

class BlockChain(models.Model):
    request_date = models.DateTimeField('Request Date', auto_now_add=True)
    respond_date = models.DateTimeField('Respond Date', auto_now= True)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, null=True, help_text='simple descripton text.')

    def respond(self):
        self.respond_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
