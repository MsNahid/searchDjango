from django.urls import path

from .import views

app_name = 'searchapp'
urlpatterns = [
    path('home/', views.home, name='home'),
]