from core_app.models import Graph
from django.shortcuts import render
from django.apps.registry import apps


def complex_visualization(request):
    graph = Graph.objects.all()[0]
    nodes = graph.nodes.all()
    edges = graph.edges.all()
    json_parser_plugin = apps.get_app_config('core_app').json_parser_plugin
    xml_parser_plugin = apps.get_app_config('core_app').xml_parser_plugin
    visualization_plugins = apps.get_app_config('core_app').visualization_plugins
    return render(request, "complex_visualization.html", {
        "nodes": nodes,
        "edges": edges,
        "json_parser_plugin": json_parser_plugin,
        "xml_parser_plugin": xml_parser_plugin,
        "visualization_plugins": visualization_plugins
    })
