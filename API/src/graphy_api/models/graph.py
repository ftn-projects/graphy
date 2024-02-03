from typing import List
from node import Node
from edge import Edge


class Graph(object):
    def __init__(self):
        self.__nodes: List[Node] = []
        self.__edges: List[Edge] = []

    @property
    def nodes(self) -> List[Node]:
        return self.__nodes

    @property
    def edges(self) -> List[Edge]:
        return self.__edges

    def add_node(self, node: Node) -> None:
        self.__nodes.append(node)

    def add_edge(self, edge: Edge) -> None:
        self.__edges.append(edge)
