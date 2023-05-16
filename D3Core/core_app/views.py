from django.apps.registry import apps
from django.shortcuts import render, redirect

from core_app.models import TestModel
from core_app.models import Graph

from core_app.models import Node
from core_app.models import Edge


def index(request):
    json_parser_plugin = apps.get_app_config('core_app').json_parser_plugin
    xml_parser_plugin = apps.get_app_config('core_app').xml_parser_plugin
    visualization_plugins = apps.get_app_config('core_app').visualization_plugins

    return render(request, "index.html", {"title": "Index",
                                          "json_parser_plugin": json_parser_plugin,
                                          "xml_parser_plugin": xml_parser_plugin,
                                          "visualization_plugins": visualization_plugins})


def load_plugin_json(request, id):
    request.session['selected_json_plugin'] = id
    plugins = apps.get_app_config('core_app').json_parser_plugin
    for i in plugins:
        if i.identifier() == id:
            i.load()
    return redirect('index')


def load_plugin_xml(request, id):
    request.session['selected_xml_plugin'] = id
    plugins = apps.get_app_config('core_app').xml_parser_plugin
    for i in plugins:
        if i.identifier() == id:
            i.load()
    return redirect('index')


# def visualize_plugin_complex(request, id):
#     request.session['selected_complex_plugin'] = id
#     plugins = apps.get_app_config('core_app').complex_visualization_plugin
#     for i in plugins:
#         if i.identifier() == id:
#             i.load()
#     return redirect('index')
#
#
# def visualize_plugin_simple(request, id):
#     request.session['selected_simple_plugin'] = id
#     plugins = apps.get_app_config('core_app').simple_visualization_plugin
#     for i in plugins:
#         if i.identifier() == id:
#             i.load()
#     return redirect('index')