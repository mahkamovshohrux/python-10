from django.urls import path 
from .views import AllList10,Idlist10

urlpatterns = [
    path("app10/",AllList10.as_view()),
    path("app10/<int:pk>",Idlist10.as_view())

]