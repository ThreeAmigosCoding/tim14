from core_app.models import Graph
from django.shortcuts import render
from django.apps.registry import apps


def simple_visualization(request):
    graph = Graph.objects.all()[0]
    root_nodes = graph.find_root_nodes()
    nodes = graph.nodes.all()
    edges = graph.edges.all()
    parser_plugins = apps.get_app_config('core_app').parser_plugins
    visualization_plugins = apps.get_app_config('core_app').visualization_plugins
    return render(request, "simple_visualization.html", {
        "root_nodes": root_nodes,
        "nodes": nodes,
        "edges": edges,
        "parser_plugins": parser_plugins,
        "visualization_plugins": visualization_plugins
    })
