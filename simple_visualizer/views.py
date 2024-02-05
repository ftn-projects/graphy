from django.shortcuts import render, redirect
import json
from API.src.graphy_api.services import visualizer_observer, EventType
from django.http import HttpResponse

last_selected_node = None


def create_graph(request, graph):
    global last_selected_node
    last_selected_node = None
    serialized_nodes = [{'id': node.id, 'value': node.value} for node in graph.nodes]
    serialized_edges = [{'source': edge.source.id, 'target': edge.destination.id, 'value': edge.value} for edge in
                        graph.edges]
    graph_data = {
        'nodes': serialized_nodes,
        'edges': serialized_edges
    }

    graph_json = json.dumps(graph_data)

    return render(request, 'create_graph.html', {'graph_json': graph_json})


def on_node_selected(request, selected_node_id):
    print("Clicked node id on this visualizer: ", selected_node_id)
    visualizer_observer.notify(EventType.NODE_SELECTED, selected_node_id)
    return HttpResponse(status=200)


def on_node_received(event, selected_node_id):
    global last_selected_node
    print("Clicked node id from an unknown source: ", selected_node_id)
    last_selected_node = selected_node_id


def return_selected_node(request):
    return HttpResponse(json.dumps({'selected_node': last_selected_node}))


visualizer_observer.attach(EventType.NODE_SELECTED, on_node_received)
