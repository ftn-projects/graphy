from __future__ import annotations

from typing import Dict, List


class Node(object):
    def __init__(self, name: str) -> None:
        self.__id: int = -1
        self.__name: str = name
        self.__properties: Dict[str, any] = {}
        self.__parent: Node | None = None
        self.__children: List[Node] = []

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, node_id: int) -> None:
        self.__id = node_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def properties(self) -> Dict[str, any]:
        return self.__properties

    @properties.setter
    def properties(self, properties: Dict[str, any]) -> None:
        self.__properties = properties

    @property
    def parent(self) -> Node | None:
        return self.__parent

    @parent.setter
    def parent(self, parent: Node) -> None:
        self.__parent = parent

    @property
    def children(self) -> List[Node]:
        return self.__children

    def add_child(self, child: Node) -> None:
        self.__children.append(child)

    def add_property(self, key: str, value: any) -> None:
        while key in self.__properties:
            key = '_' + key
        self.__properties[key] = value

    def clone(self) -> Node:
        n = Node(self.name)
        n.id = self.id
        n.properties = {}
        for k, v in self.properties.items():
            n.properties[k] = v
        return n

    def __str__(self) -> str:
        properties_str = ', '.join(f'{key}={value}' for key, value in self.__properties.items())
        return f"\nNode <{self.__name}>:\n  - {properties_str}"

    def __repr__(self) -> str:
        properties_str = ', '.join(f'{key}={value}' for key, value in self.__properties.items())
        return f"\nNode <{self.__name}>:\n  - {properties_str}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Node):
            return False
        return self.name == other.name and self.dict_eq(self.properties, other.properties)

    def __hash__(self) -> int:
        return hash((self.name, self.hashable_dict(self.properties)))

    @staticmethod
    def dict_eq(dict1, dict2):
        """Recursively checks dictionary equality."""
        if dict1.keys() != dict2.keys():
            return False
        for key in dict1:
            if dict1[key] != dict2[key]:
                return False
        return True

    @staticmethod
    def hashable_dict(d):
        """Converts a dictionary into a hashable form by recursively processing its content."""
        return frozenset((key, value) for key, value in sorted(d.items()))
