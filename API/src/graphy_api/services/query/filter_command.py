from typing import Tuple

from .command import Command
from ...models import Graph
from ..util_service import UtilService


class FilterCommand(Command):
    def __init__(self, graph: Graph, query: Tuple[str, str, str]):
        self.__query = query
        self.__parse = UtilService().parse_any

        if self.operator not in ["=", "<", "<=", ">", ">=", "!="]:
            raise ValueError("operator is not supported")

        super().__init__(graph)

    @property
    def value(self) -> str:
        return self.__query[0]

    @property
    def operator(self) -> str:
        return self.__query[1]

    @property
    def parameter(self) -> any:
        return self.__parse(self.__query[2])

    def fulfills(self, value_name: str, attribute_value: any) -> bool:
        return value_name == self.value and any([
            self.operator == "=" and attribute_value == self.parameter,
            self.operator == "<" and attribute_value < self.parameter,
            self.operator == "<=" and attribute_value <= self.parameter,
            self.operator == ">" and attribute_value > self.parameter,
            self.operator == ">=" and attribute_value >= self.parameter,
            self.operator == "!=" and attribute_value != self.parameter
        ])
