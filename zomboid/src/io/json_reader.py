from pathlib import Path
import json
from src.io.file_reader import AbstractReader
from src.io.model import DataModel


class JSONReader(AbstractReader):
    def __init__(self, path: Path):
        self.path = path
        self.dic_header: dict[str, int] = {}
        
    def read(self) -> list[DataModel]:
        with open(self.path) as file:
            items_data: list[dict[str, object]] = json.load(file)
            if not items_data:
                return []

            dic_data: dict[str, object] = items_data[0]
            self.dic_header = {key: idx for idx, key in enumerate(dic_data.keys())}

            items = [
                DataModel(
                    id=int(item['id']),
                    name=item['name'],
                    type_object=item['type_object'],
                    condition=item['condition'],
                    amount=int(item['amount'])
                ) for item in items_data
            ]
        return items
    
    def get_header(self) -> dict[str, int]:
        return self.dic_header
