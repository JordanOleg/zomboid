import csv
from pathlib import Path
from src.model import DataModel
from src.io.file_reader import AbstractReader


class CSVReader(AbstractReader):
    """
    A reader class for parsing CSV files and converting data into DataModel objects.
    """
    def __init__(self, path: Path):
        """
        Initializes the CSVReader with the file path.

        Args:
            path (Path): Path to the CSV file to be read.
        """
        self.path: Path = path
        self.dic_header: dict[str, int] = {}
    
    def read(self) -> list[DataModel]:
        """
        Reads the CSV file and converts its content into a list of DataModel objects.

        Returns:
            list[DataModel]: A list of DataModel objects parsed from the CSV file.
        """
        result: list[DataModel] = []
        with open(self.path) as csv_file:
            spam_reader = csv.reader(csv_file)
            self.dic_header = {}
            head = next(spam_reader)
            i = 0
            for item in head:
                self.dic_header[item] = i
                i+=1
            for row in spam_reader:
                data = DataModel(id=int(row[self.dic_header["id"]]), name=row[self.dic_header["name"]],
                                 type_object=row[self.dic_header["type_object"]], condition=row[self.dic_header["condition"]], 
                                 amount=int(row[self.dic_header["amount"]]))
                result.append(data)
            return result
        
    def get_header(self) -> dict[str, int]:
        """
        Returns the headers of the CSV file as a dictionary.

        Returns:
            dict[str, int]: A dictionary where keys are column names and values are their indices.
        """
        return self.dic_header
