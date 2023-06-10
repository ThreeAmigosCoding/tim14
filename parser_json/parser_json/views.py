from django.apps.registry import apps
from django.shortcuts import redirect
from .code.parse_code_json import JsonParser


def parser_json(request, file):
    parser = JsonParser()
    parser.load(file)
    return redirect("/visualization/simple")
