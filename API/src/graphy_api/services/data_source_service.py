from abc import abstractmethod
from graphy_api.services.service_base import ServiceBase
from graphy_api.services.source_reader.source_reader import SourceReader


class DataSourceService(ServiceBase):
    def __init__(self):
        self.__reader: SourceReader = None

    @property
    def reader(self) -> SourceReader:
        return self.__reader

    @reader.setter
    def reader(self, reader) -> None:
        self.__reader = reader

    @abstractmethod
    def identifier(self):
        pass

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def load(self):
        pass
