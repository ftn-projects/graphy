from graphy_api.models import Graph, Node, Edge
from graphy_api.services import DataSourceService
import xml.etree.ElementTree as eT


class XmlDataSourceService(DataSourceService):
    def _load_string(self, text: str) -> Graph:
        graph = Graph()
        tree = eT.ElementTree(eT.fromstring(text))

        tree_root = tree.getroot()
        root = self.parse_node(tree_root, graph)
        graph.add_node(root)
        self.cyclic_graph(graph)
        return graph

    def identifier(self) -> str:
        return "XmlDataSourceService"

    def name(self) -> str:
        return "XML source"

    def parse_node(self, root: eT.Element, graph: Graph) -> Node:
        node = Node(root.tag)
        self.parse_attributes(root, node, graph)
        for child in root:
            if child.text is not None and child.text.strip() != "":
                node.add_property(self.string_cleanup(child.tag), self.string_cleanup(child.text))
                self.parse_attributes(child, node, graph, child.tag)
            else:
                result = self.parse_node(child, graph)
                node.add_child(result)
                result.parent = node
                graph.add_node(result)
                graph.add_edge(Edge(node, result))
        return node

    def parse_attributes(self, tree_node: eT.Element, node: Node, graph: Graph, prefix: str = None):
        for k, v in tree_node.attrib.items():
            if k == "reference":
                node.add_property(k, v)
                continue

            exists = graph.find_node(v)
            if exists is not None:
                if prefix is not None:
                    graph.add_edge(Edge(node, exists, prefix + "(" + k + ")"))
                else:
                    graph.add_edge(Edge(node, exists, k))
            else:
                new_node = Node(v)
                graph.add_node(new_node)
                if prefix is not None:
                    graph.add_edge(Edge(node, new_node, prefix + "(" + k + ")"))
                else:
                    graph.add_edge(Edge(node, new_node, k))

    def cyclic_graph(self, graph: Graph):
        removed = []
        for node in graph.nodes:
            if "reference" in node.value:
                referenced = self.find_reference(node, node.value["reference"])
                graph.add_edge(Edge(node.parent, referenced))
                graph.remove_edge(Edge(node.parent, node))
                removed.append(node)

        for n in removed:
            graph.remove_node(n)

    def find_reference(self, node: Node, ref: str) -> Node:
        spliced = ref.split("/")
        steps = len(spliced) - 1
        for _ in range(steps):
            node = node.parent

        kids = node.children
        node_tag = spliced[-1].split("[")[0]
        order = spliced[-1].split('[')[1][:-1]

        filtered = [n for n in kids if n.id == node_tag]
        return filtered[int(order) - 1]

    def string_cleanup(self, text: str) -> str:
        text.replace("\n", "")
        tokens = text.split()
        return " ".join(tokens)
