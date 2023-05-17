from django.urls import path
from . import views

urlpatterns = [
    path('visualization/complex', views.complex_visualization, name="complex_visualization")
]
