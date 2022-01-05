from django.urls import path
from . import views
# from addlist import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('newlist/', views.newlist, name='newlist'),
    
]
