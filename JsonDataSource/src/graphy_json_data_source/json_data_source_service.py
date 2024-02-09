from graphy_api.models import Graph, Node, Edge
from graphy_api.services import DataSourceService
from .json_error import JsonError
import json as jsonutil


class JsonDataSourceService(DataSourceService):
    def __init__(self):
        super().__init__()
        self.__graph: Graph | None = None
        self.__id_mark = '@id'

    def _load_string(self, text: str) -> Graph:
        self.__graph = Graph()

        json = jsonutil.loads(text)
        self.__construct_tree(json)
        self.__connect_marked_nodes()
        self.__cleanup_marked_properties()

        return self.__graph

    def __construct_tree(self, json: any):
        self.__load_object('', json, None)

    def __load_object(self, key: str, json: any, parent: Node | None, parent_obj: bool = True) -> None:
        if isinstance(json, dict):
            node = self.__create_with_parent(key, parent)
            self.__load_dictionary(node, json.items())
        elif isinstance(json, list):
            if parent_obj:
                node = parent
            else:  # parent is list too so the new node is created
                node = self.__create_with_parent(key, parent)
                key = ''
            self.__load_list(node, [(key, v) for v in json])
        else:
            raise JsonError(json)

    def __load_dictionary(self, node: Node, items: iter) -> None:
        for k, v in items:
            if isinstance(v, str):
                node.add_property(k, v)
            else:
                self.__load_object(k, v, node)

    def __load_list(self, node: Node, items: iter) -> None:
        for k, v in items:
            if isinstance(v, str):
                self.__create_with_parent(k, node, v)
            else:
                self.__load_object(k, v, node, False)

    def __create_with_parent(self, key: str, parent: Node | None, name: str = '') -> Node:
        node = Node(name)
        self.__graph.add_node(node)

        if parent is not None:
            parent.add_child(node)
            node.parent = parent
            self.__graph.add_edge(Edge(parent, node, key))

        return node

    def __connect_marked_nodes(self):
        for node in self.__graph.nodes:
            for k, v in node.properties.items():
                if k[0] == '@' and k != self.__id_mark:
                    connected = self.__find_node_by_reference(v)
                    node.add_child(connected)
                    self.__graph.add_edge(Edge(node, connected, k[1:]))

    def __find_node_by_reference(self, ref: str) -> Node:
        mark = self.__id_mark
        for node in self.__graph.nodes:
            if mark in node.properties and node.properties[mark] == ref:
                return node
        raise ValueError(f'reference: \'{ref}\' does not exist')

    def __cleanup_marked_properties(self):
        for node in self.__graph.nodes:
            for k in [k for k in node.properties if k[0] == '@']:
                node.properties.pop(k)

    @staticmethod
    def identifier() -> str:
        return 'JSON'

    @staticmethod
    def name() -> str:
        return 'json data source'
