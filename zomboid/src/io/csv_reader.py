import csv
from pathlib import Path
from src.io.model import DataModel
from src.io.file_reader import AbstractReader


class CSVReader(AbstractReader):
    def __init__(self, path: Path):
        self.path: Path = path
        self.dic_header: dict[str, int] = {}
    
    def read(self) -> list[DataModel]:
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
                data = DataModel(id=row[self.dic_header["id"]], name=row[self.dic_header["name"]],
                                 type_object=row[self.dic_header["type"]], condition=row[self.dic_header["condition"]], 
                                 amount=row[self.dic_header["amount"]])
                result.append(data)
            return result
        
    def get_header(self) -> dict[str, int]:
        return self.dic_header
