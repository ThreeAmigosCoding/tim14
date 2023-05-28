from django.db import models


class Graph(models.Model):
    name = models.CharField(max_length=255)

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
