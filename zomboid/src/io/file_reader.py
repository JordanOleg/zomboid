from abc import ABC, abstractmethod
from pathlib import Path


class AbstractReader(ABC):

    @abstractmethod
    def read(self, path: Path):
        pass

