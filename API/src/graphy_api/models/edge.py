from .node import Node


class Edge(object):
    def __init__(self, source: Node, destination: Node, value: str = None):
        self.__source: Node = source
        self.__destination: Node = destination
        self.__value: str = value

    @property
    def source(self) -> Node:
        return self.__source

    @property
    def destination(self) -> Node:
        return self.__destination

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        self.__value = value

    def __str__(self) -> str:
        return f"Grana(<{self.source.id}> <{self.value}> <{self.destination.id}>)"

    def __repr__(self) -> str:
        return f"Grana(<{self.source.id}> <{self.value}> <{self.destination.id}>)"

    def __eq__(self, other) -> bool:
        if isinstance(other, Edge):
            return (self.source, self.destination, self.value) == (other.source, other.destination, other.value)
        return False

    def __hash__(self) -> int:
        return hash((self.source, self.destination, self.value))
