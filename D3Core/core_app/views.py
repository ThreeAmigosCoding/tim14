from django.apps.registry import apps
from django.db.models import Q
from django.shortcuts import render, redirect

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


def search_graph(request, layout_type, query_string):
    filtered_nodes = Node.objects.filter(Q(data__name__icontains=query_string) | Q(data__value__icontains=query_string))
    Node.objects.exclude(pk__in=filtered_nodes).update(enabled=False)
    Edge.objects.filter(Q(start_node__enabled=False) | Q(end_node__enabled=False)).update(enabled=False)
    return redirect("/visualization/" + layout_type)


def filter_graph(request, layout_type, operation):
    attribute_name = operation.split(" ")[0].strip()
    operator = operation.split(" ")[1].strip()
    operand = operation.split(" ")[2].strip()

    # filter logic

    with open("log.txt", "a") as f:
        f.write(str(attribute_name) + "\n")
        f.write(str(operator) + "\n")
        f.write(str(operand) + "\n")

    return redirect("/visualization/" + layout_type)

def reset_graph(request, layout_type):
    Node.objects.all().update(enabled=True)
    Edge.objects.all().update(enabled=True)
    return redirect("/visualization/" + layout_type)
