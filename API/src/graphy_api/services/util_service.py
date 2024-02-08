from dateutil.parser import parse
from datetime import datetime



class UtilService:
    def __init__(self, dateformat: str = None) -> None:
        self.__dateformat = dateformat

    def parse_any(self, value: str) -> any:
        funcs = [int, float, self.parse_date]
        for f in funcs:
            try:
                return f(value)
            except ValueError:
                pass
        return value

    def parse_date(self, value: str) -> datetime:
        if self.__dateformat is not None:
            return datetime.strptime(value, self.__dateformat)
        return parse(value, fuzzy='true')
