from django.urls import path
from . import views
app_name='whether'
urlpatterns = [
path('', views.index),
]