import json

from core_app.services.load import LoadService

from core_app.models import Graph
from core_app.models import Node
from core_app.models import Edge
from core_app.models import Attribute
from datetime import datetime


class JsonParser(LoadService):

    def __init__(self):
        self.node_id = 0
        self.id_map = {}
        self.reference_map = {}

    def name(self):
        return "JSON parser"

    def identifier(self):
        return "parse_json"

    def load(self, file):
        self.parse_json_to_graph(self.load_from_file(file))

    def parse_json_to_graph(self, json_data):
        Graph.objects.all().delete()
        self.id_map = {}
        self.reference_map = {}
        graph = Graph.objects.create(name="MyGraph")
        self.parse_json(graph, json.loads(json_data))

        for node, reference in self.reference_map.items():
            if reference in self.id_map:
                Edge.objects.create(
                    graph=graph,
                    start_node=node,
                    end_node=self.id_map[reference]
                )

        return graph

    def parse_json(self, graph, data, parent_node=None, key_name="Root"):
        if isinstance(data, dict):
            node = Node.objects.create(node_id=self.node_id, name=key_name, graph=graph)
            for keym, valuem in data.items():
                if not isinstance(valuem, (dict, list)):
                    Attribute.objects.create(node=node, name=keym, value=valuem,
                                             value_type=self.get_variable_type(valuem))
                    if keym == "id":
                        self.id_map[valuem] = node
                    if keym == "references":
                        self.reference_map[node] = valuem
            self.node_id += 1
            if parent_node:
                Edge.objects.create(graph=graph, start_node=parent_node, end_node=node)
            for key, value in data.items():
                self.parse_json(graph, value, node, key)
        elif isinstance(data, list):
            if self.check_list_type(data) == "Primitive":
                Attribute.objects.create(node=parent_node, name=key_name, value=data,
                                         value_type=self.get_variable_type(data))
            else:
                for item in data:
                    self.parse_json(graph, item, parent_node, key_name)

    def check_list_type(self, data):
        if isinstance(data, list):
            for item in data:
                return self.check_list_type(item)
        elif isinstance(data, dict):
            return "Dictionary"
        else:
            return "Primitive"

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

    def test_json_data(self):
        return '''
                {
                  "graph": {
                    "person": [
                      {
                        "id": "1",
                        "references": "1",
                        "name": "Milos",
                        "age": "2023-03-03",
                        "address": {
                          "street": "123 Main St",
                          "city": "New York"
                        }
                      },
                      {
                        "id": "2",
                        "references": "3",
                        "name": "Alice",
                        "age": "32",
                        "address": {
                          "street": "456 Elm St",
                          "city": "Los Angeles"
                        }
                      },
                      {
                        "id": "3",
                        "references": "1",
                        "name": "Alice",
                        "age": "32",
                        "address": {
                          "street": "456 Elm St",
                          "city": "Los Angeles"
                        }
                      },
                      {
                        "id": "4",
                        "references": "1",
                        "name": "Aliaaaaaaaace",
                        "age": "32",
                        "address": {
                          "street": "aaaaaaaaa",
                          "city": "Novi Sad"
                        }
                      }
                    ]
                  }
                }
        '''

    def load_from_file(self, file):
        with open("files/" + file, 'r', encoding='utf-8') as f:
            file_contents = f.read()
        return file_contents
