from graphy_api.models import Graph, Node, Edge
from graphy_api.services import DataSourceService
from rdflib import Graph as RDFGraph, Literal, URIRef


class RdfDataSourceService(DataSourceService):
    def _load_string(self, text: str) -> Graph:
        g = RDFGraph()
        g.parse(data=text, format="turtle")

        graph = Graph()

        for subject, predicate, obj in g:
            # Check if the subject node is already in the graph, if not, add it
            subject_node = Node(str(subject))
            if subject_node not in graph.nodes:
                graph.add_node(subject_node)
            else:
                subject_node = graph.nodes[graph.nodes.index(subject_node)]

            # Check if the predicate is already present in the subject node's properties, if not, add it
            if predicate not in subject_node.value:
                # Create a new URIRef or Literal depending on the type of obj
                if isinstance(obj, Literal):
                    subject_node.add_property(str(predicate), obj.toPython())
                elif isinstance(obj, URIRef):
                    obj_node = Node(obj)
                    # Check if the obj node is already in the graph, if not, add it
                    if obj_node not in graph.nodes:
                        graph.add_node(obj_node)
                    # Create an edge between the subject and obj nodes, if it doesn't exist
                    edge = Edge(subject_node, obj_node, str(predicate))
                    if edge not in graph.edges:
                        graph.add_edge(edge)

        return graph

    def identifier(self) -> str:
        return "RdfDataSourceService"

    def name(self) -> str:
        return "RDF source"
