from django.conf.urls import url
 
from .import views

urlpatterns=[
      url(r'^$',views.index,name='index'),
      url(r'^home/',views.home,name='home'),
      url(r'^contact/',views.contact,name='contact'),
];
