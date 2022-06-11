from django.urls import path
from .import views

urlpatterns=[
    path('',views.display),
    path('signup',views.signup),
    path('login',views.main),
    path('submit',views.info),
    path('upload',views.details),
    path('update',views.update),
    path('updatenewbook',views.modify),
    path('delete',views.delete),
    path('showdelete',views.showdelete),
    path('retrive',views.retrive),
    path('retrivedata',views.retrivedata)
    
    ]