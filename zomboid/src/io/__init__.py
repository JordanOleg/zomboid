from pathlib import Path
from typing import List, Iterable
from src.io.printer_model import PrinterModel
from src.io.csv_reader import CSVReader
from src.io.file_reader import AbstractReader
from src.io.model import DataModel, get_dict_data_models



class Zomboid:
    def __init__(self, source_model: list[DataModel], dic_model: dict[str, int] = None):
        self.data_model: list[DataModel] = source_model
        self.dic_model: dict[str, int] = dic_model if dic_model is None else get_dict_data_models()
        
    def print_models(self):
        reader = PrinterModel(
            self.data_model, 
            self.dic_model, 
            )
        reader.print()
