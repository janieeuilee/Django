from django.urls import path
from django.conf.urls import url
from enterprise.views import EnterpriseRLV, EnterpriseALV
from . import views 
app_name = 'ent'

urlpatterns = [
    # path('list/', EnterpriseLV.as_view(), name='ent_list'),
    path('request_ls', EnterpriseRLV.as_view(), name='request_ls'),
    path('approve_list', EnterpriseALV.as_view(), name='approve_list'),
    # path('add', views.InputForm, name= 'data_add'),
]
