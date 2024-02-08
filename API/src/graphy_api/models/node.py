from __future__ import annotations

from typing import Dict, List


class Node(object):
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__value: Dict[str, any] = {}
        self.__parent: Node | None = None
        self.__children: List[Node] = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def value(self) -> Dict[str, any]:
        return self.__value

    @value.setter
    def value(self, value: Dict[str, any]) -> None:
        self.__value = value

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

    def add_property(self, predicate: str, value: any) -> None:
        self.__value[predicate] = value

    def __str__(self) -> str:
        properties_str = ', '.join(f'{key}={value}' for key, value in self.__value.items())
        return f"\nNode <{self.__name}>:\n  - {properties_str}"

    def __repr__(self) -> str:
        properties_str = ', '.join(f'{key}={value}' for key, value in self.__value.items())
        return f"\nNode <{self.__name}>:\n  - {properties_str}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Node):
            return False
        return self.name == other.name and self.dict_eq(self.value, other.value)

    def __hash__(self) -> int:
        return hash((self.name, self.hashable_dict(self.value)))

    @staticmethod
    def dict_eq(dict1, dict2):
        """Recursively checks dictionary equality."""
        if dict1.keys() != dict2.keys():
            return False
        for key in dict1:
            val1, val2 = dict1[key], dict2[key]
            if isinstance(val1, dict) and isinstance(val2, dict):
                if not Node.dict_eq(val1, val2):
                    return False
            elif val1 != val2:
                return False
        return True

    @staticmethod
    def hashable_dict(d):
        """Converts a dictionary into a hashable form by recursively processing its content."""
        def hashable_value(value):
            if isinstance(value, dict):
                return Node.hashable_dict(value)
            elif isinstance(value, list):
                return tuple(map(hashable_value, value))
            else:
                return value
        return frozenset((key, hashable_value(value)) for key, value in sorted(d.items()))
