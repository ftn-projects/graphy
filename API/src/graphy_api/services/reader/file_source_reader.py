from . import SourceReader
import os


class FileSourceReader(SourceReader):

    def __init__(self, filepath: str):
        self.__filepath: str = filepath

    def read(self) -> str:
        if os.path.isfile(self.__filepath):
            raise FileNotFoundError(f"{self.__filepath} does not exist.")

        with open(self.__filepath) as f:
            return f.read()
