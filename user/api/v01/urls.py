from django.conf.urls import url
from django.urls import path, include
from .views import create,logout,logout_all
app_name = 'user'

urlpatterns = [
    path('api/users/', create, name='create-user'),
    path('api/users/logout/', logout, name='logout-user'),
    path('api/users/logout-all/', logout_all, name='logout-all-users'),
]