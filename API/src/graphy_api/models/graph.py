from __future__ import annotations
from typing import List
from .node import Node
from .edge import Edge


class Graph(object):
    def __init__(self) -> None:
        self.__nodes: List[Node] = []
        self.__edges: List[Edge] = []

    @property
    def nodes(self) -> List[Node]:
        return self.__nodes

    @property
    def edges(self) -> List[Edge]:
        return self.__edges

    def add_node(self, node: Node) -> None:
        node.id = self.size + 1
        self.__nodes.append(node)

    def add_edge(self, edge: Edge) -> None:
        self.__edges.append(edge)

    def remove_node(self, node: Node) -> None:
        node.parent.children.remove(node)
        self.__nodes.remove(node)

    def remove_edge(self, edge: Edge) -> None:
        self.__edges.remove(edge)

    def find_node(self, tag: str) -> Node | None:
        for node in self.__nodes:
            if node.name == tag:
                return node
        return None

    @property
    def size(self) -> int:
        return len(self.nodes)

    def get_unordered(self) -> Graph:
        g = Graph()
        for node in self.__nodes:
            g.add_node(node.clone())
        for edge in self.__edges:
            if edge not in g.edges and edge.reversed() not in g.edges:
                g.add_edge(edge.clone())
        return g
