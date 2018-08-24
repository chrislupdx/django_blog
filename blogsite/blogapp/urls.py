from django.urls import path
from . import views

app_name = 'blogapp' # for namespacing
urlpatterns = [
    path('', views.index, name='index')
]

