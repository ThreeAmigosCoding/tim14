from core_app.models import Graph, Node, Edge, Attribute
from core_app.services.load import LoadService
import xml.etree.ElementTree as ET


class XmlParser(LoadService):

    def __init__(self):
        self.node_id = 0

    def name(self):
        return "XML parser"

    def identifier(self):
        return "parse_xml"

    def load(self):
        self.parse_xml_to_graph(self.test_xml_data())

    def parse_xml_to_graph(self, xml_string):
        root = ET.fromstring(xml_string)

        graph = Graph.objects.create(name='Graph')

        nodes = {}

        def parse_element(elem, parent=None):
            node = Node.objects.create(
                graph=graph,
                name=elem.tag,
                node_id=self.node_id
            )
            self.node_id += 1

            if not list(elem) and elem.text != '':
                Attribute.objects.create(
                    name='value',
                    value=elem.text,
                    node=node
                )

            for attr, value in elem.attrib.items():
                Attribute.objects.create(
                    name=attr,
                    value=value,
                    node=node
                )

            nodes[node.pk] = node

            if parent is not None:
                Edge.objects.create(
                    graph=graph,
                    start_node=parent,
                    end_node=node
                )
            for child in elem:
                parse_element(child, node)

        parse_element(root)

        return graph

    def test_xml_data(self):
        return '''
                <root>
                    <name>John Smith</name>
                    <age value1='30'>30</age>
                    <address>
                        <city>New York</city>
                        <state>NY</state>
                    </address>
                </root>
                '''
