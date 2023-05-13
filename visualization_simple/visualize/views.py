from D3Core.core_app.models import Node, Edge
from django.apps.registry import apps
from django.shortcuts import render


def simple_visualization(request):
    nodes = Node.objects.all()
    edges = Edge.objects.all()
    return render(request, "simple_visualization.html", {
                                          "nodes": nodes,
                                          "edges": edges})
