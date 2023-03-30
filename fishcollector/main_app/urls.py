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

# FISH ADD PLANTS ROUTE
path('fish/<int:fish_id>/assoc_plants/<int:plants_id>/', views.assoc_plants, name='assoc_plants'),

# PLANTS INDEX ROUTE
    path('plants/', views.plants_index, name='plants_index'),

# PLANTS DETAILS ROUTE
    path('plants/<int:plants_id>/', views.plants_details, name='plants_details'),

# PLANTS CREATE ROUTE
    path('plants/create/', views.PlantsCreate.as_view(), name='plants_create'),

# PLANTS UPDATE ROUTE
    path('plants/<int:pk>/update', views.PlantsUpdate.as_view(), name='plants_update'),

# PLANTS DELETE ROUTE
    path('plants/<int:pk>/delete', views.PlantsDelete.as_view(), name='plants_delete'),
]