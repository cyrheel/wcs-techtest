from django.urls import path
from . import views

app_name = 'DynaForm'
urlpatterns = [
    path('', views.get_name, name='name')
]
