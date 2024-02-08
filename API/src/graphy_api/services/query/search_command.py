from .command import Command
from ...models import Graph


class SearchCommand(Command):
    def __init__(self, graph: Graph, param: str):
        super().__init__(graph)
        self.__param = param

    def fulfills(self, value_name: str, attribute: any) -> bool:
        return self.__param in str(value_name) or self.__param in str(attribute)

