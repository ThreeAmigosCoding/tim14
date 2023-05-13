import json

from core_app.models import TestModel
from core_app.services.load import LoadService

from core_app.models import Graph
from core_app.models import Node

from core_app.models import Edge


class JsonParser(LoadService):

    def __init__(self):
        self.node_id = 0

    def name(self):
        return "JSON parser"

    def identifier(self):
        return "parse_json"

    def load(self):
        self.parse_json_to_graph(self.test_json_data())

    def parse_json_to_graph(self, json_data):
        graph = Graph.objects.create(name="MyGraph")

        def parse_json(data, parent_node=None):
            if isinstance(data, dict):
                json_data_new = {}
                for keym, valuem in data.items():
                    if not isinstance(valuem, (dict, list)):
                        json_data_new[keym] = valuem
                node = Node.objects.create(node_id=self.node_id, name="Node", graph=graph, data=json_data_new)
                self.node_id += 1
                if parent_node:
                    Edge.objects.create(graph=graph, start_node=parent_node, end_node=node)
                for key, value in data.items():
                    parse_json(value, node)
            elif isinstance(data, list):
                for item in data:
                    parse_json(item, parent_node)

        parse_json(json.loads(json_data))
        return graph

    def test_json_data(self):
        return '{"name": "John Smith", "age": 30, "address": {"city": "New York", "state": "NY"}}'
