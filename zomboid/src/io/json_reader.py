from src.io.file_reader import AbstractReader
from pathlib import Path
import json.encoder


class JSONReader(AbstractReader):
    def read(self, path: Path) -> list[dict[str, str]]:
        with path.open() as file:
            data = json.load(file)
            return data
