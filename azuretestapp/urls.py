from django.urls import include, path
from . import views

urlpatterns = [
    path('testing', views.TestView.as_view() , name='test') 

]