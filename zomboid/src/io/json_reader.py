from pathlib import Path
import json
from src.io.file_reader import AbstractReader
from src.model import DataModel


class JSONReader(AbstractReader):
    """
    A reader class for parsing JSON files and converting data into DataModel objects.
    """
    def __init__(self, path: Path):
        """
        Initializes the JSONReader with the file path.

        Args:
            path (Path): Path to the JSON file to be read.
        """
        self.path = path
        self.dic_header: dict[str, int] = {}
        
    def read(self) -> list[DataModel]:
        """
        Reads the JSON file and converts its content into a list of DataModel objects.

        Returns:
            list[DataModel]: A list of DataModel objects parsed from the JSON file.

        Process:
            - Opens and loads the JSON file as a list of dictionaries.
            - Extracts headers from the first dictionary and stores them in `dic_header`.
            - Converts each dictionary into a DataModel instance.
        """
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
        """
        Returns the headers of the JSON file as a dictionary.

        Returns:
            dict[str, int]: A dictionary where keys are the attribute names and values are their indices.
        """
        return self.dic_header
