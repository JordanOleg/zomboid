from pathlib import Path
import json
from src.io.file_reader import AbstractReader
from src.io.model import DataModel


class JSONReader(AbstractReader):
    def __init__(self, path: Path):
        self.path = path
        self.dic_header = {}
        
    def read(self) -> list[DataModel]:
        with open(self.path) as file:
            items_data: list[dict[str, object]] = json.load(file)
            if not items_data:
                return []
            dic_data: dict[str, object] = items_data[0]
            zip_data = zip(dic_data.keys(), range(len(dic_data.keys())))
            self.dic_header = dict(zip_data)
            items = [DataModel(**item) for item in items_data]
        return items
    
    def get_header(self) -> dict[str, int]:
        return self.dic_header
