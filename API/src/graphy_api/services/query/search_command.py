from .command import Command
from ...models import Graph


class SearchCommand(Command):
    def __init__(self, graph: Graph, param: str):
        super().__init__(graph)
        self.__param = param

    def fulfills(self, attribute_key: str, attribute_value: any) -> bool:
        return self.__param in attribute_key.lower() or self.__param in str(attribute_value).lower()

    def serialize(self) -> str:
        return self.__param

