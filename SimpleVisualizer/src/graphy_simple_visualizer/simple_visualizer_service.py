import json
from datetime import datetime

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from graphy_api import Graph
from graphy_api.services import VisualizerService


class SimpleVisualizerService(VisualizerService):
    def create_view(self, request: WSGIRequest, graph: Graph = None) -> HttpResponse:
        if graph is None:
            # Handle case when graph is not provided
            graph_data = {'nodes': [], 'edges': []}  # Default or empty graph data
            graph_json = json.dumps(graph_data)
            return render(request, 'create_graph.html', {'graph_json': graph_json})

        formatted_nodes = []
        for node in graph.nodes:
            n = node.clone()
            for k, v in node.properties.items():
                if isinstance(v, datetime):
                    n.properties[k] = str(v)
            formatted_nodes.append(n)

        serialized_nodes = [{'id': node.id, 'name': node.name, 'properties': node.properties}
                            for node in formatted_nodes]
        serialized_edges = [{'source': edge.source.id, 'target': edge.destination.id, 'value': edge.value}
                            for edge in graph.edges]
        graph_data = {
            'nodes': serialized_nodes,
            'edges': serialized_edges
        }

        graph_json = json.dumps(graph_data)
        graph_json = graph_json.replace('\'', '\\\'')

        return render(request, 'create_graph.html', {'graph_json': graph_json})

    @staticmethod
    def identifier() -> str:
        return 'SIMPLE'

    @staticmethod
    def name() -> str:
        return 'Simple Visualizer'
