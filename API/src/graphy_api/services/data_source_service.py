from abc import abstractmethod
from graphy_api.services import ServiceBase
from graphy_api.services.reader import SourceReader


class DataSourceService(ServiceBase):
    def __init__(self):
        self.__reader: SourceReader | None = None

    @property
    def reader(self) -> SourceReader | None:
        return self.__reader

    @reader.setter
    def reader(self, reader: SourceReader) -> None:
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
