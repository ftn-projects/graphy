from abc import ABC, abstractmethod


class ServiceBase(ABC):
    @staticmethod
    @abstractmethod
    def identifier() -> str:
        pass

    @staticmethod
    @abstractmethod
    def name() -> str:
        pass
