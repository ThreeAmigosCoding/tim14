from django.apps.registry import apps
from django.shortcuts import render, redirect


def index(request):
    #plugini = apps.get_app_config('core_app').parser_plugins
    return render(request, "index.html", {"title": "Index"})
