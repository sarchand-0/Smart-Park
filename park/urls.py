from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
	path('',views.home, name="home"),
    path('Dashboard/',views.dashboard, name="dash"),
    path('Location1/',views.Location1, name="loc1"),
    path('AboutUs/',views.AboutUs, name="AboutUs"),
    path('Reserve/',views.Reserve, name="Reserve"),
    path('vid/',views.vid, name="vid"),
    ]