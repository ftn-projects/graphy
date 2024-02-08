from django.shortcuts import render, redirect
import json

last_selected_node = None
last_zoom_level = None


def create_graph(request, graph=None):
    global last_selected_node

    if graph is None:
        # Handle case when graph is not provided
        graph_data = {'nodes': [], 'edges': []}  # Default or empty graph data
        graph_json = json.dumps(graph_data)
        return render(request, 'create_block_graph.html', {'graph_json': graph_json})

    last_selected_node = None
    serialized_nodes = [{'name': node.name, 'value': node.value} for node in graph.nodes]
    serialized_edges = [{'source': edge.source.name, 'target': edge.destination.name, 'value': edge.value} for edge in
                        graph.edges]
    graph_data = {
        'nodes': serialized_nodes,
        'edges': serialized_edges
    }

    graph_json = json.dumps(graph_data)

    return render(request, 'create_block_graph.html', {'graph_json': graph_json})
