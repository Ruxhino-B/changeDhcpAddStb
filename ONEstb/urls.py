from django.urls import path
from .views import changeHexRandreply, loginapp, logout_view


urlpatterns = [
    path('', changeHexRandreply, name='onestb'),
    path('login/', loginapp, name='login'),
    path('logout/', logout_view, name='logout')
    ]