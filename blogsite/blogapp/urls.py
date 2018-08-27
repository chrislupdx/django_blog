from django.urls import path, include
from . import views

app_name = 'blogapp' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
	path('add_comment/', views.add_comment, name='add_comment'),

#not sure what foreignkey we're passing there
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]