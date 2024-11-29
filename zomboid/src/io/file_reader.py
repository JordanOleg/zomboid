from abc import ABC, abstractmethod
from pathlib import Path
from src.model import DataModel

class AbstractReader(ABC):
    """
    An abstract base class for all readers (e.g., CSVReader, XMLReader, JSONReader).
    This class defines the common interface that all reader classes must implement.

    The purpose of this class is to enforce a contract that any specific reader
    will provide implementations for the methods `read` and `get_header`, which are
    used to process data from a file and extract the header information, respectively.
    """
    @abstractmethod
    def read(self) -> list[DataModel]:
        """
        Reads data from a file and returns it as a list of DataModel objects.
        
        Returns:
            list[DataModel]: A list of DataModel objects parsed from the file.
        
        This method must be implemented by all subclasses of AbstractReader.
        """
        pass
    
    @abstractmethod
    def get_header(self) -> dict[str, int]:
        """
        Returns the header information from the file as a dictionary mapping column names
        to their corresponding indices.

        Returns:
            dict[str, int]: A dictionary where the keys are column names and the values are their indices.

        This method must be implemented by all subclasses of AbstractReader.
        """
        pass
