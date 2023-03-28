from django.urls import path
from . import views

# ROUTES ARE HERE
urlpatterns = [
# HOME ROUTE
    path('', views.home, name='home'),
#ABOUT ROUTE
    path('about/', views.about, name='about'),
#INDEX ROUTE
    path('fish/', views.fish_index, name='index'),
]
