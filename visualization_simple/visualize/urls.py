from django.urls import path
from . import views

urlpatterns = [
    path('visualization/simple',views.simple_visualization, name="simple_visualization")
]