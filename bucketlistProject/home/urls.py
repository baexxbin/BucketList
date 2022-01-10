from django.urls import path
from . import views
# from addlist import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.login, name='login'),
    # path('newlist/',views.newlist, name='newlist'),
]
