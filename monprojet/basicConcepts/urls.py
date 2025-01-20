from django.urls import path
from . import views
urlpatterns=[
    #path("",views.welcome, name="welsome"),
    path("",views.home, name="home"),
    #path("user",views.User, name="user")
    path("resultat",views.result, name="result")
]