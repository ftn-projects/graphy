from abc import ABC, abstractmethod
from ...models import Graph


class Command(ABC):
    def __init__(self, graph: Graph):
        self._graph = graph

    def query(self) -> Graph:
        result = Graph()
        for node in self._graph.nodes:
            for k, v in node.properties.items():
                if self.fulfills(k, v):
                    result.add_node(node)
                    break

        for node in self._graph.nodes:
            children = []
            for child in node.children:
                if child in result.nodes:
                    children.append(child)
            node.children = children

        for edge in self._graph.edges:
            if edge.source in result.nodes and edge.destination in result.nodes:
                result.add_edge(edge)

        return result

    @abstractmethod
    def fulfills(self, attribute_key: str, attribute_value: any) -> bool:
        pass

    @abstractmethod
    def serialize(self) -> str:
        pass
