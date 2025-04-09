from django.urls import path
from atv1 import views 

urlpatterns = [
    path('', views.firstpage, name='firstpage'),

]
