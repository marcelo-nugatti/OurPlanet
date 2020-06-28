from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='home'),
        path('i_love_you_;)_<3/', views.weightEnd, name='end'),
        
]
