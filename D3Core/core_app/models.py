from django.db import models


class Graph(models.Model):
    name = models.CharField(max_length=255)

    def find_root_nodes(self):
        root_nodes = []

        subgraphs = self.find_non_connected_subgraphs()
        for subgraph in subgraphs:
            cyclic = True
            for node in subgraph:
                if not self.edges.filter(end_node=node).exists():
                    root_nodes.append(node)
                    cyclic = False
                    break
            if cyclic:
                node_children_count = sum(1 for edge in self.edges.filter(start_node=list(subgraph)[0]))
                max_children_node = list(subgraph)[0]
                for node in subgraph:
                    subgraph_node_children_count = sum(1 for edge in self.edges.filter(start_node=node))
                    if subgraph_node_children_count > node_children_count:
                        max_children_node = node
                        node_children_count = subgraph_node_children_count
                root_nodes.append(max_children_node)

        return root_nodes

    def find_non_connected_subgraphs(self):
        subgraphs = []
        visited = set()
        nodes = self.nodes.all()

        def dfs(node):
            stack = [node]
            subgraph_nodes = set()

            while stack:
                current_node = stack.pop()
                visited.add(current_node)
                subgraph_nodes.add(current_node)

                edges = self.edges.filter(start_node=current_node)
                for edge in edges:
                    if edge.end_node not in visited:
                        stack.append(edge.end_node)

            subgraphs.append(subgraph_nodes)

        for node in nodes:
            if node not in visited:
                dfs(node)

        return subgraphs

    def __str__(self):
        return self.name


class Node(models.Model):
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE, related_name='nodes')
    node_id = models.IntegerField(default=-1)
    name = models.CharField(max_length=255)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Edge(models.Model):
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE, related_name='edges')
    start_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='start_node')
    end_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='end_node')
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.start_node.name + " --- " + self.end_node.name


class Attribute(models.Model):
    name = models.CharField(max_length=1023)
    value = models.CharField(max_length=1023)
    value_type = models.CharField(max_length=255, default="str")
    node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='data')

    def __str__(self):
        return str(self.name) + ": " + str(self.value)
