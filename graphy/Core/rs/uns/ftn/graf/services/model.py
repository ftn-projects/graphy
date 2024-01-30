class Graf:
    def __init__(self):
        self.__nodes = []
        self.__edges = []

    @property
    def nodes(self):
        return self.__nodes

    @property
    def edges(self):
        return self.__edges

    def add_node(self, node):
        self.__nodes.append(node)

    def add_edge(self, edge):
        self.__edges.append(edge)


class Cvor:
    def __init__(self, uri):
        self.__uri = uri
        self.__properties = {}

    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, value):
        self.__uri = value

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, value):
        self.__properties = value

    def add_property(self, predicate, value):
        self.__properties[predicate] = value

    def __str__(self):
        properties_str = ', '.join(f'{key}={value}' for key, value in self.__properties.items())
        return f"\nNode <{self.__uri}>:\n  - {properties_str}"

    def __repr__(self):
        properties_str = ', '.join(f'{key}={value}' for key, value in self.__properties.items())
        return f"\nNode <{self.__uri}>:\n  - {properties_str}"

    def __eq__(self, other):
        if isinstance(other, Cvor):
            return self.uri == other.uri
        return NotImplemented

    def __hash__(self):
        return hash(self.uri)


class Grana:
    def __init__(self, izvor, cilj, oznaka=None):
        self.__izvor = izvor
        self.__cilj = cilj
        self.__oznaka = oznaka

    @property
    def izvor(self):
        return self.__izvor

    @property
    def cilj(self):
        return self.__cilj

    @property
    def oznaka(self):
        return self.__oznaka

    @oznaka.setter
    def oznaka(self, vrednost):
        self.__oznaka = vrednost

    def __str__(self):
        return f"Grana(<{self.izvor.uri}> <{self.oznaka}> <{self.cilj.uri}>)"

    def __repr__(self):
        return f"Grana(<{self.izvor.uri}> <{self.oznaka}> <{self.cilj.uri}>)"

    def __eq__(self, other):
        if isinstance(other, Grana):
            return (self.izvor, self.cilj, self.oznaka) == (other.izvor, other.cilj, other.oznaka)
        return NotImplemented

    def __hash__(self):
        return hash((self.izvor, self.cilj, self.oznaka))
