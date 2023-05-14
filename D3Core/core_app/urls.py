from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # Kada korisnik pogodi ovaj endpoint (http://127.0.0.1:8000/ucitavanje/plugin/ucitati_prodavnice_kod),
    # doci ce do ucitavanja plugina, ciji je identifikator "ucitati_prodavnice_kod".

    path('ucitavanje/json/plugin/<str:id>', views.load_plugin_json, name="json_parse_plugin"),
    path('ucitavanje/xml/plugin/<str:id>', views.load_plugin_xml, name="xml_parse_plugin"),
]