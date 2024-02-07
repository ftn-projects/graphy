from typing import Dict


class Node(object):
    def __init__(self, node_id: str):
        self.__id: str = node_id
        self.__value: Dict[str, any] = {}
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, node_id: str) -> None:
        self.__id = node_id

    @property
    def value(self) -> Dict[str, any]:
        return self.__value

    @value.setter
    def value(self, value: Dict[str, any]) -> None:
        self.__value = value

    def add_property(self, predicate: str, value: any) -> None:
        self.__value[predicate] = value

    def __str__(self) -> str:
        properties_str = ', '.join(f'{key}={value}' for key, value in self.__value.items())
        return f"\nNode <{self.__id}>:\n  - {properties_str}"

    def __repr__(self) -> str:
        properties_str = ', '.join(f'{key}={value}' for key, value in self.__value.items())
        return f"\nNode <{self.__id}>:\n  - {properties_str}"

    def __eq__(self, other) -> bool:
        if isinstance(other, Node):
            return self.id == other.id
        return False

    def __hash__(self) -> int:
        return hash(self.id)
