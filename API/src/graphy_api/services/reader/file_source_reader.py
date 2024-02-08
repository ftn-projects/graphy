from . import SourceReader
import os


class FileSourceReader(SourceReader):

    def __init__(self, filepath: str):
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"{filepath} does not exist.")

        self.__filepath: str = filepath

    def read(self) -> str:
        with open(self.__filepath) as f:
            return f.read()
