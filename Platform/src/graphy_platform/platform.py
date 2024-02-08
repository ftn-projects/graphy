from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from graphy_api.services import *
from graphy_api.services.reader import *
from graphy_api.models import *

from graphy_json_data_source import *
from graphy_xml_data_source import *
from graphy_rdf_data_source import *

from graphy_simple_visualizer import *


data_source_services = {
    JsonDataSourceService.identifier(): JsonDataSourceService(),
    XmlDataSourceService.identifier(): XmlDataSourceService(),
    RdfDataSourceService.identifier(): RdfDataSourceService()
}

visualizer_services = {
    SimpleVisualizerService.identifier(): SimpleVisualizerService()
}


class Platform:
    def __init__(self):
        self.__source_plugin: DataSourceService | None = None
        self.__visualizer_plugin: VisualizerService | None = None
        self.__graph: Graph | None = None

    def load_graph(self) -> None:
        self.__graph = self.__source_plugin.load()

    def render_graph(self, request: WSGIRequest) -> HttpResponse:
        return self.__visualizer_plugin.create_view(request, self.__graph)

    def set_sources(self, filepath: str, data_source: str, visualizer: str):
        if data_source in data_source_services:
            self.__source_plugin = data_source_services[data_source]
        else:
            raise ValueError('unknown data source type')
        if visualizer in visualizer_services:
            self.__visualizer_plugin = visualizer_services[visualizer]
        else:
            raise ValueError('unknown visualizer type')

        reader = FileSourceReader(filepath)
        self.__source_plugin.set_reader(reader)
        self.__source_plugin.set_util(UtilService())
