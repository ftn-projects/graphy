from abc import ABC, abstractmethod


class SourceReader(ABC):
    @abstractmethod
    def read(self) -> str:
        pass
