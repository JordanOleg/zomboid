from pathlib import Path
from typing import List, Iterable
from src.io.reader_model import ReaderModel
from src.io.csv_reader import CSVReader
from src.io.model import DataModel



class Zomboid:
    def __init__(self, reader: CSVReader, skip: int, take: int):
        self.reader = reader
        self.skip = skip
        self.take = take

    def print_models(self):
        reader = ReaderModel(
            self.reader.read(), 
            self.reader.dic_data, 
            self.skip, self.take
            )
        reader.print()
        
    def set_skip(self, skip: int):
        self.skip = skip

    def set_take(self, take: int):
        self.take = take
