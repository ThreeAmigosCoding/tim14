from core_app.models import Graph, Node, Edge
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

        # Create a new Graph object
        graph = Graph.objects.create(name='Graph')

        # create a dictionary to store the nodes
        nodes = {}
        # recursive function that will traverse the xml tree
        def parse_element(elem, parent=None):
            data = elem.attrib
            if not list(elem) and elem.text != '':
                data['value'] = elem.text
            # Create a new Node object
            node = Node.objects.create(
                graph=graph,
                name=elem.tag,
                data=data,
                node_id=self.node_id
            )
            self.node_id +=1
            nodes[node.pk] = node

            # Create an Edge object if parent is not None
            if parent is not None:
                edge = Edge.objects.create(
                    graph=graph,
                    start_node=parent,
                    end_node=node
                )
            # iterate over the children of the current element
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



