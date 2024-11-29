from pathlib import Path
from typing import List, Iterable
from src.printer_model import PrinterModel
from src.io.csv_reader import CSVReader
from src.io.file_reader import AbstractReader
from src.model import DataModel, default_dict_models


class Zomboid:
    """
    A class designed to print all data models to the console using a specified format.

    Attributes:
        data_model (list[DataModel]): The list of DataModel objects to be printed.
        dic_model (dict[str, int]): A dictionary representing column headers and their order. 
                                    Defaults to a predefined dictionary if not provided.
    """
    def __init__(self, source_model: list[DataModel], dic_model: dict[str, int] = None):
        """
        Initializes the Zomboid class with the data models and dictionary for table headers.

        Args:
            source_model (list[DataModel]): The list of DataModel objects to be printed.
            dic_model (dict[str, int], optional): A dictionary of table headers and their positions. 
                                                  Defaults to `default_dict_models`.
        """
        self.data_model: list[DataModel] = source_model
        self.dic_model: dict[str, int] = dic_model if dic_model else default_dict_models
        
    def print_models(self):
        """
        Prints all data models to the console in a tabular format using the PrinterModel class.
        """
        reader = PrinterModel(
            self.data_model, 
            self.dic_model, 
            )
        reader.print()