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

#SHOW ROUTE
    path('fish/<int:fish_id>/', views.fish_detail, name='detail'),

# CREATE ROUTE
    path('fish/create/', views.FishCreate.as_view(), name='fish_create'),

# UPDATE ROUTE
    path('fish/<int:pk>/update/', views.FishUpdate.as_view(), name='fish_update'),

# DELETE ROUTE
    path('fish/<int:pk>/delete/', views.FishDelete.as_view(), name='fish_delete'),

# FEEDING ROUTE
    path('fish/<int:fish_id>/add_feeding/', views.add_feeding, name='add_feeding'),

# PLANTS INDEX ROUTE
    path('plants/', views.plants_index, name='plants_index'),

# PLANTS DETAILS ROUTE
    path('plants/<int:plants_id>/', views.plants_details, name='plants_details'),

# PLANTS CREATE ROUTE
    path('plants/create/', views.PlantsCreate.as_view(), name='plants_create'),
]