from abc import ABC, abstractmethod
from pathlib import Path
from src.io.model import DataModel

class AbstractReader(ABC):

    @abstractmethod
    def read(self) -> list[DataModel]:
        pass
    
    @abstractmethod
    def get_header(self) -> dict[str, int]:
        pass
