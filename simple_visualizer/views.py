from django.shortcuts import render
import json
import random
from API.src.graphy_api import  Graph, Node, Edge
# Create your views here.
def create_graph(request):
    graph = Graph()

    # Define the number of nodes and edges in the graph
    num_nodes = 20
    num_edges = 30

    # Create nodes with random names
    for i in range(num_nodes):
        node = Node(str(i), {"name": f"Node {i}"})
        graph.add_node(node)

    # Create random edges between nodes
    for _ in range(num_edges):
        source_node = random.choice(graph.nodes)
        destination_node = random.choice(graph.nodes)
        while source_node == destination_node:  # Ensure no self-loops
            destination_node = random.choice(graph.nodes)
        edge = Edge(source_node, destination_node, f"Edge from {source_node.id} to {destination_node.id}")
        graph.add_edge(edge)

    serialized_nodes = [{'id': node.id, 'value': node.value} for node in graph.nodes]
    serialized_edges = [{'source': edge.source.id, 'target': edge.destination.id, 'value': edge.value} for edge in
                        graph.edges]

    graph_data = {
        'nodes': serialized_nodes,
        'edges': serialized_edges
    }

    # Convert the graph data to JSON string
    graph_json = json.dumps(graph_data)

    return render(request, 'create_graph.html', {'graph_json': graph_json})