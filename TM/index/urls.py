from django.conf.urls import url 
from django.urls import path
from index import views

urlpatterns = [
    path('', views.start, name = 'start'),
    path('finish/', views.finish, name = 'finish'),
    path('record/', views.record, name = 'record')
]