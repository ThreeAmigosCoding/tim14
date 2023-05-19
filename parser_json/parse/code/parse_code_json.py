import json

from core_app.services.load import LoadService

from core_app.models import Graph
from core_app.models import Node
from core_app.models import Edge
from core_app.models import Attribute


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
                node = Node.objects.create(node_id=self.node_id, name="Node", graph=graph)
                for keym, valuem in data.items():
                    if not isinstance(valuem, (dict, list)):
                        Attribute.objects.create(node=node, name=keym, value=valuem)
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
        data = []
        for i in range(20):
            main_obj = {
                "id": i,
                "name": f"Main Object {i}",
                "nested_objects": []
            }
            for j in range(3):
                nested_obj = {
                    "id": f"{i}_{j}",
                    "name": "Nested Obj abcd abvgddjez 123456 Nested Obj abcd abvgddjez 123456"
                }
                main_obj["nested_objects"].append(nested_obj)
            data.append(main_obj)
        return json.dumps(data)
