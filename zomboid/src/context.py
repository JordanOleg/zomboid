from pathlib import Path
from src.model import DataModel
from src.io.file_reader import AbstractReader
from src.io.csv_reader import CSVReader
from src.io.json_reader import JSONReader
from src.io.xml_reader import XMLReader


class Context:
    def __init__(self, path: Path):
        self.path = path
        self._reader = None
        
    def get_reader(self) -> AbstractReader:
        file_extension = self.path.suffix.lower()
        
        if file_extension == '.xml':
            self._reader = XMLReader(self.path)
            return self._reader
        elif file_extension == '.csv':
            self._reader = CSVReader(self.path)
            return self._reader
        elif file_extension == '.json':
            self._reader = JSONReader(self.path)
            return self._reader
        else:
            raise ValueError("Unsupported file format")
        
    def get_model(self) -> list[DataModel]:
        if self._reader:
            result = self._reader.read()
        else:
            self._reader = self.get_reader()
            result = self._reader.read()
        return result
    
    def get_header(self) -> dict[str, int]:
        if self._reader:
            result = self._reader.get_header()
        else:
            self._reader = self.get_reader()
            result = self._reader.get_header()
        return result
