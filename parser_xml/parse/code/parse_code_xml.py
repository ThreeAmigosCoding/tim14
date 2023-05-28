from core_app.models import Graph, Node, Edge, Attribute
from core_app.services.load import LoadService
import xml.etree.ElementTree as ET
from datetime import datetime


class XmlParser(LoadService):

    def __init__(self):
        self.node_id = 0
        self.id_map = {}
        self.reference_map = {}

    def name(self):
        return "XML parser"

    def identifier(self):
        return "parse_xml"

    def load(self):
        self.parse_xml_to_graph(self.test_xml_data())

    def parse_xml_to_graph(self, xml_string):
        root = ET.fromstring(xml_string)
        Graph.objects.all().delete()
        self.id_map = {}
        self.reference_map = {}
        graph = Graph.objects.create(name='Graph')
        nodes = {}
        self.parse_element(graph, nodes, root)

        for node, reference in self.reference_map.items():
            if reference in self.id_map:
                Edge.objects.create(
                    graph=graph,
                    start_node=node,
                    end_node=self.id_map[reference]
                )

        return graph

    def parse_element(self, graph, nodes, elem, parent=None):
        node = Node.objects.create(
            graph=graph,
            name=elem.tag,
            node_id=self.node_id
        )
        self.node_id += 1

        if not list(elem) and (elem.text is not None and elem.text.strip().replace("\n", " ")):
            Attribute.objects.create(
                name='value',
                value=elem.text.strip().replace("\n", " "),
                value_type=self.get_variable_type(elem.text.strip().replace("\n", " ")),
                node=node
            )

        for attr, value in elem.attrib.items():
            Attribute.objects.create(
                name=attr,
                value=value,
                value_type=self.get_variable_type(value),
                node=node
            )

            if attr == "id":
                self.id_map[value] = node
            if attr == "references":
                self.reference_map[node] = value

        nodes[node.pk] = node

        if parent is not None:
            Edge.objects.create(
                graph=graph,
                start_node=parent,
                end_node=node
            )

        for child in elem:
            self.parse_element(graph, nodes, child, node)

    def get_variable_type(self, string):

        try:
            value = eval(string)
            return type(value).__name__
        except (NameError, SyntaxError):
            if self.is_date_string(string):
                return "datetime"
            return "str"

    def is_date_string(self, string):
        date_formats = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"]  # Add more formats if needed
        for date_format in date_formats:
            try:
                datetime.strptime(string, date_format)
                return True
            except ValueError:
                pass
        return False

    def test_xml_data(self):
        return '''
                <graph>
                    <person id="1" references="1">
                        <name>Milos</name>
                        <age>28</age>
                        <address>
                            <street>123 Main St</street>
                            <city>New York</city>
                        </address>
                    </person>
                    <person id="2" references="3">
                        <name>Alice</name>
                        <age>32</age>
                        <address>
                            <street>456 Elm St</street>
                            <city>Los Angeles</city>
                        </address>
                    </person>
                    <person id="3" references="1">
                        <name>Alice</name>
                        <age>32</age>
                        <address>
                            <street>456 Elm St</street>
                            <city>Los Angeles</city>
                        </address>
                    </person>
                </graph>
                '''
