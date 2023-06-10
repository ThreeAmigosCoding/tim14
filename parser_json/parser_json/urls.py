from . import views
from django.urls import path

urlpatterns = [
    path('parser/json/<str:file>', views.parser_json, name="parser_json")
]