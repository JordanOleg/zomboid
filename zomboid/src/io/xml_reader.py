from xml.etree import ElementTree
from pathlib import Path
from src.io.file_reader import AbstractReader
from src.model import DataModel


class XMLReader(AbstractReader):
    def __init__(self, path: Path, root: str = "Item"):
        self.path: Path = path
        self.dic_header: dict[str, int] = {}
        self.tree_root: str = root
    
    def read(self) -> list[DataModel]:
        items = []
        tree = ElementTree.parse(self.path)
        root = tree.getroot()
        first_item = root.find(self.tree_root)
        if first_item is not None:
            keys = [child.tag for child in first_item]
            self.dic_header = dict(zip(keys, range(len(keys))))

        for item in root.findall(self.tree_root):
            item_data = {child.tag: child.text for child in item}
            items.append(DataModel(id=int(item_data["id"]), name=item_data["name"], 
                                   condition=item_data["condition"], type_object=item_data["type_object"], 
                                   amount=int(item_data["amount"])))
        return items
    
    def get_header(self) -> dict[str, int]:
        return self.dic_header