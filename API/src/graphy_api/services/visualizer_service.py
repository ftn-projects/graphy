from abc import abstractmethod, ABCMeta

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

from .service_base import ServiceBase
from ..models.graph import Graph


class VisualizerService(ServiceBase, metaclass=ABCMeta):
    @abstractmethod
    def create_view(self, request: WSGIRequest, graph: Graph = None) -> HttpResponse:
        pass
