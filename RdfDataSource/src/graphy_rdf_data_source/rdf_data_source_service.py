from graphy_api.models import Graph, Node, Edge
from graphy_api.services import DataSourceService
from rdflib import Graph as RDFGraph, Literal, URIRef


class RdfDataSourceService(DataSourceService):
    def _load_string(self, text: str) -> Graph:
        g = RDFGraph()
        g.parse(data=text, format="xml")

        graph = Graph()

        for subject, predicate, obj in g:
            # Check if the subject node is already in the graph, if not, add it
            subject_node = Node(str(subject))

            is_node_in_graph = False
            for node in graph.nodes:
                if node.name == subject_node.name:
                    is_node_in_graph = True
                    subject_node = node
                    break

            if not is_node_in_graph:
                graph.add_node(subject_node)

            # Check if the predicate is already present in the subject node's properties, if not, add it
            if predicate not in subject_node.properties:
                # Create a new URIRef or Literal depending on the type of obj
                if isinstance(obj, Literal):
                    subject_node.add_property(str(predicate), obj.toPython())
                elif isinstance(obj, URIRef):
                    obj_node = Node(str(obj))
                    # Check if the obj node is already in the graph, if not, add it

                    is_node_in_graph = False
                    for node in graph.nodes:
                        if node.name == obj_node.name:
                            is_node_in_graph = True
                            obj_node = node
                            break

                    if not is_node_in_graph:
                        graph.add_node(obj_node)

                    # Create an edge between the subject and obj nodes, if it doesn't exist
                    edge = Edge(subject_node, obj_node, str(predicate))
                    if edge not in graph.edges:
                        graph.add_edge(edge)
                        subject_node.add_child(obj_node)

        return graph


    @staticmethod
    def identifier() -> str:
        return "RDF"

    @staticmethod
    def name() -> str:
        return "rdf data source"
