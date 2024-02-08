from django.shortcuts import render
from graphy_simple_visualizer import create_graph as plugin_create_graph
from graphy_api import Graph, Node, Edge
import random

graph = Graph()

# Define the number of nodes and edges in the graph
num_nodes = 200
num_edges = 250

# Create nodes with random names
for i in range(num_nodes):
    node_properties = {"name": f"Node {i}"}
    node = Node(str(i))
    node.value = node_properties

    graph.add_node(node)

# Create random edges between nodes
for _ in range(num_edges):
    source_node = random.choice(graph.nodes)
    destination_node = random.choice(graph.nodes)
    while source_node == destination_node:  # Ensure no self-loops
        destination_node = random.choice(graph.nodes)
    edge = Edge(source_node, destination_node, f"Edge from {source_node.name} to {destination_node.name}")
    graph.add_edge(edge)


def home(request):
    global graph
    response = plugin_create_graph(request, graph)
    plugin_content = response.content.decode()

    return render(request, 'platform_home.html', {'plugin_content': plugin_content})
