from abc import abstractmethod, ABCMeta
from .service_base import ServiceBase
from .util_service import UtilService
from .reader.source_reader import SourceReader
from ..models.graph import Graph


class DataSourceService(ServiceBase, metaclass=ABCMeta):
    def __init__(self):
        self.__reader: SourceReader | None = None
        self.__util: UtilService | None = None

    def set_reader(self, reader: SourceReader) -> None:
        self.__reader = reader

    def set_util(self, util: UtilService) -> None:
        self.__util = util

    def load(self) -> Graph:
        return self._load_string(self.__reader.read())

    @abstractmethod
    def _load_string(self, text: str) -> Graph:
        pass
