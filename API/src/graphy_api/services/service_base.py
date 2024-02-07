from abc import ABC, abstractmethod


class ServiceBase(ABC):
    @abstractmethod
    def identifier(self) -> str:
        pass

    @abstractmethod
    def name(self) -> str:
        pass
