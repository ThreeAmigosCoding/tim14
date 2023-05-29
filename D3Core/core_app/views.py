from datetime import datetime

from django.apps.registry import apps
from django.db.models import Q
from django.http import HttpResponseBadRequest
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
    valid_operators = ['<', '<=', '==', '>', '>=', '!=']

    attribute_name = operation.split(" ")[0].strip()
    if not attribute_name:
        return HttpResponseBadRequest("Invalid attribute name")

    operator = operation.split(" ")[1].strip()
    if not operator or operator not in valid_operators:
        return HttpResponseBadRequest("Invalid operator")

    operand = operation.split(" ")[2].strip()
    if not operand:
        return HttpResponseBadRequest("Invalid operand")

    operand_type = get_variable_type(operand)

    if operand_type == "str" and operator != '==' and operator != '!=':
        return HttpResponseBadRequest("Invalid operand type")

    all_nodes = Node.objects.filter(Q(data__name__iexact=attribute_name) & Q(data__value_type__iexact=operand_type))
    nodes = []
    for node in all_nodes:
        if node.enabled:
            nodes.append(node)

    Node.objects.all().update(enabled=False)
    Edge.objects.all().update(enabled=False)

    for node in nodes:
        for atr in node.data.all():
            if atr.name == attribute_name:
                attribute_value = convert(atr.value, atr.value_type)
                operand_value = convert(operand, operand_type)
                compare(attribute_value, operand_value, operator, node)
                break
    Edge.objects.filter(Q(start_node__enabled=True) & Q(end_node__enabled=True)).update(enabled=True)

    return redirect("/visualization/" + layout_type)


def reset_graph(request, layout_type):
    Node.objects.all().update(enabled=True)
    Edge.objects.all().update(enabled=True)
    return redirect("/visualization/" + layout_type)


def compare(a, b, operator, node):
    if operator == "!=":
        if a != b:
            Node.objects.filter(pk__iexact=node.pk).update(enabled=True)
    elif operator == "<=":
        if a <= b:
            Node.objects.filter(pk__iexact=node.pk).update(enabled=True)
    elif operator == ">=":
        if a >= b:
            Node.objects.filter(pk__iexact=node.pk).update(enabled=True)
    elif operator == "==":
        if a == b:
            Node.objects.filter(pk__iexact=node.pk).update(enabled=True)
    elif operator == "<":
        if a < b:
            Node.objects.filter(pk__iexact=node.pk).update(enabled=True)
    elif operator == ">":
        if a > b:
            Node.objects.filter(pk__iexact=node.pk).update(enabled=True)


# region Helper Functions
def get_variable_type(string):
    try:
        value = eval(string)
        return type(value).__name__
    except (NameError, SyntaxError):
        if is_date_string(string):
            return "datetime"
        return "str"


def is_date_string(string):
    date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"]  # Add more formats if needed
    for date_format in date_formats:
        try:
            datetime.strptime(string, date_format)
            return True
        except ValueError:
            pass
    return False


def convert_to_date_format(string):
    date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"]  # Add more formats if needed
    for date_format in date_formats:
        try:
            date_object = datetime.strptime(string, date_format)
            return date_object
        except ValueError:
            pass
    return None


def convert(value, value_type):
    if value_type == "int":
        return int(value)
    elif value_type == "float":
        return float(value)
    elif value_type == "datetime":
        return convert_to_date_format(value)
    else:
        return str(value)

# endregion
