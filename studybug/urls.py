
from django.urls import path, include

from studybug.views import home

urlpatterns = [
    path('',home,name='home')
]