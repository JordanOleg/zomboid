from pathlib import Path
from src.model import DataModel
from src.io.file_reader import AbstractReader
from src.io.csv_reader import CSVReader
from src.io.json_reader import JSONReader
from src.io.xml_reader import XMLReader


class Context:
    """
    A class that implements the Strategy design pattern for reading and handling files with different formats.

    This class selects an appropriate reader (strategy) based on the file's extension 
    and delegates the tasks of reading data and headers to the chosen reader.

    Attributes:
        path (Path): The file path pointing to the file to be read.
        _reader (AbstractReader): The reader strategy chosen dynamically based on the file format.
    """
    def __init__(self, path: Path):
        """
        Initializes the Context with a file path.

        Args:
            path (Path): The file path to be processed.
        """
        self.path = path
        self._reader = None
        
    def get_reader(self) -> AbstractReader:
        """
        Determines and returns the appropriate reader strategy based on the file extension.

        Returns:
            AbstractReader: An instance of the appropriate reader (e.g., XMLReader, CSVReader, JSONReader).
        
        Raises:
            ValueError: If the file format is unsupported.
        """
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
        """
        Reads the file and returns a list of DataModel objects by using the chosen reader strategy.

        Returns:
            list[DataModel]: A list of deserialized DataModel objects.
        """
        if self._reader:
            result = self._reader.read()
        else:
            self._reader = self.get_reader()
            result = self._reader.read()
        return result
    
    def get_header(self) -> dict[str, int]:
        """
        Retrieves the headers of the file using the chosen reader strategy.

        Returns:
            dict[str, int]: A dictionary representing the headers of the file and their positions.
        """
        if self._reader:
            result = self._reader.get_header()
        else:
            self._reader = self.get_reader()
            result = self._reader.get_header()
        return result
