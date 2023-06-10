from django.shortcuts import redirect
from .code.parse_code_xml import XmlParser


def parser_xml(request, file):
    parser = XmlParser()
    parser.load(file)
    return redirect("/visualization/simple")
