from django.db import models


class Graph(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Node(models.Model):
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    data = models.JSONField()

    def __str__(self):
        return self.name


class Edge(models.Model):
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
    start_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='start_node')
    end_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='end_node')

    def __str__(self):
        return self.start_node.name + " --- " + self.end_node.name


class TestModel(models.Model):
    name = models.CharField(max_length=50)
    greeting = models.CharField(max_length=50)