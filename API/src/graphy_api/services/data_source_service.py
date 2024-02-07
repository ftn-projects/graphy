from abc import abstractmethod, ABCMeta
from graphy_api.services import ServiceBase
from graphy_api.services.reader import SourceReader
from graphy_api.models import Graph


class DataSourceService(ServiceBase, metaclass=ABCMeta):
    def init(self):
        self.reader: SourceReader | None = None

    @property
    def reader(self) -> SourceReader | None:
        return self.reader

    @reader.setter
    def reader(self, reader: SourceReader) -> None:
        self.reader = reader

    def load(self) -> Graph:
        return self._load_string(self.reader.read())

    @abstractmethod
    def _load_string(self, text: str) -> Graph:
        pass
