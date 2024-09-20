from django.urls import path
from . import views

urlpatterns = [
    path("school-data/", views.school_data_view, name='school_data_view'),
    path("school-data/index.html", views.school_data_view, name='school_data_view'),
    path("school-data/awards.html", views.Award, name='Award'),
    path("school-data/about.html", views.about, name='about'),
    
]


