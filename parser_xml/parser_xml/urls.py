from . import views
from django.urls import path

urlpatterns = [
    path('parser/xml/<str:file>', views.parser_xml, name="parser_xml")
]