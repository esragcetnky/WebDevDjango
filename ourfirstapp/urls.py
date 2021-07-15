from django.conf.urls import url

from ourfirstapp import views

urlpatterns=[    
    url("/date/",views.my_app),
    url('/first/',views.first),
    url('/second/',views.second),
    url('/third/',views.third),
    url('/fourth/',views.fourth),
]