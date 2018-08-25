from django.urls import path, include
from . import views

app_name = 'blogapp' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]