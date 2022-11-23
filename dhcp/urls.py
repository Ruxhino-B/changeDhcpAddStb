from django.urls import path
from .views import IpPoolsListView, PassDataBetweenTable
urlpatterns = [
    path('', IpPoolsListView.as_view(), name='ippools'),
    path('passdata', PassDataBetweenTable, name='passdata')

    ]