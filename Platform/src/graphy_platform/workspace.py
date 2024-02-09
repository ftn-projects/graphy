import json
from typing import List
import time

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from graphy_api.services import *
from graphy_api.services.reader import *
from graphy_api.models import *

from graphy_json_data_source import *
from graphy_xml_data_source import *
from graphy_rdf_data_source import *

from graphy_simple_visualizer import *
from graphy_block_visualizer import *

from graphy_api.services.query import *

data_source_services = {
    JsonDataSourceService.identifier(): JsonDataSourceService(),
    XmlDataSourceService.identifier(): XmlDataSourceService(),
    RdfDataSourceService.identifier(): RdfDataSourceService()
}

visualizer_services = {
    SimpleVisualizerService.identifier(): SimpleVisualizerService(),
    BlockVisualizerService.identifier(): BlockVisualizerService()
}


class Workspace:
    def __init__(self):
        self.__id: int = int(time.time())
        self.__filepath: str | None = ''
        self.__source_plugin: DataSourceService | None = data_source_services['XML']
        self.__visualizer_plugin: VisualizerService | None = visualizer_services['SIMPLE']
        self.__graph: Graph | None = None
        self.__initial_graph: Graph | None = None
        self.__applied_queries: List[Command] = []

    @property
    def id(self) -> int:
        return self.__id

    @property
    def filepath(self) -> str:
        return self.__filepath

    @filepath.setter
    def filepath(self, filepath: str) -> None:
        self.__filepath = filepath
        self.__source_plugin.set_reader(FileSourceReader(filepath))

    @property
    def source_plugin(self) -> DataSourceService:
        return self.__source_plugin

    @property
    def visualizer_plugin(self) -> VisualizerService:
        return self.__visualizer_plugin

    @property
    def applied_queries(self) -> List[Command]:
        return self.__applied_queries

    def load_graph(self) -> None:
        self.__graph = self.__source_plugin.load()
        self.__initial_graph = self.__source_plugin.load()

    def render_graph_view(self, request: WSGIRequest) -> HttpResponse:
        return self.__visualizer_plugin.create_view(request, self.__graph)

    def render_tree_view(self, request: WSGIRequest) -> HttpResponse:
        if self.__graph is None:
            graph_data = {'nodes': [], 'edges': []}
            graph_json = json.dumps(graph_data)
            return render(request, 'tree_view.html', {'graph': graph_json})

        serialized_nodes = [{'id': node.id, 'name': node.name, 'properties': node.properties} for node in
                            self.__graph.nodes]
        serialized_edges = [{'source': edge.source.id, 'target': edge.destination.id, 'value': edge.value} for edge in
                            self.__graph.edges]
        graph_data = {
            'nodes': serialized_nodes,
            'edges': serialized_edges
        }

        graph_json = json.dumps(graph_data)
        return render(request, 'tree_view.html', {'graph': graph_json})

    def set_source_plugin(self, data_source: str) -> None:
        if data_source in data_source_services:
            self.__source_plugin = data_source_services[data_source]
        else:
            raise ValueError('unknown data source type')

    def set_visualizer_plugin(self, visualizer: str) -> None:
        if visualizer in visualizer_services:
            self.__visualizer_plugin = visualizer_services[visualizer]
        else:
            raise ValueError('unknown visualizer type')

    def is_not_set(self) -> bool:
        return self.__source_plugin is None or self.__visualizer_plugin is None

    def search_graph(self, search: str) -> None:
        scom = SearchCommand(self.__graph, search)
        self.__graph = scom.query()
        self.__applied_queries.append(scom)

    def filter_graph(self, attribute: str, operator: str, parameter: str) -> None:
        fcom = FilterCommand(self.__graph, (attribute, operator, parameter))
        self.__graph = fcom.query()
        self.__applied_queries.append(fcom)

    def reset_graph(self):
        self.__graph = self.__initial_graph
        self.__applied_queries = []
