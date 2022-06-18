from django.urls import path, include
from . import views 
urlpatterns = [
    path('shows', views.index),
    path("new", views.add_show),
    path("submit_show", views.submit_show),
    path("display_show/<int:id>", views.display_show),
    path("edit_show/<int:id>", views.edit_show),
    path("submit_edit/<int:id>", views.submit_edit),
    path("delete_show/<int:id>", views.delete_show),
]