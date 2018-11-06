
from django.conf.urls import url
from django.urls import path
from individual.views import *
from mysite.views import HomeView



app_name = 'individual'

urlpatterns = [
    path('request_add', IndividualCreateView.as_view(), name='request_add'),
    # path('list/', EnterpriseLV.as_view(), name='ent_list'),
 # /indivisual/
    path('', PostLV.as_view(), name='index'),

    # /indivisual/post
    path('post/', PostLV.as_view(), name='post_list'),

    # /indivisual/post/python-programming
    path('post/<str:slug>', PostDV.as_view(), name='post_detail'),

    # Example: indivisual/archive/
    path('post/archive/', PostAV.as_view(), name='post_archive'),

    # Example: indivisual/2012/
    path('post/<int:year>/', PostYAV.as_view(), name='post_year_archive'),

    # Example: indivisual/2012/nov/
    path('post/<int:year>/<str:month>/', PostAV.as_view(), name='post_month_archive'),

    # Example: indivisual/2012/nov/10/
    path('post/<int:year>/<str:month>/<int:day>/', PostDAV.as_view(), name='post_day_archive'),

    # # Example: /today/
    # path('post/today/', PostTAV.as_view(), name='post_today_archive'),

    # Example: /search/
    
   
    path('back', HomeView.as_view(), name='back'),
    path('back/', HomeView.as_view(), name='back'),
    path('request_add', IndividualCreateView.as_view(), name='request_add'),


    # path('add/', PostCreateView.as_view(), name='add'),
    # path('change/', PostChangeLV.as_view(), name='change'),
    # path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
]

