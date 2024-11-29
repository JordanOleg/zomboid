from xml.etree import ElementTree
from pathlib import Path
from src.io.file_reader import AbstractReader
from src.model import DataModel


class XMLReader(AbstractReader):
    """
    A reader class for parsing XML files and extracting data into DataModel objects.

    Attributes:
        path (Path): The path to the XML file.
        dic_header (dict[str, int]): A dictionary mapping XML element tags to their positions.
        tree_root (str): The name of the root element or the parent element containing data items.
    """
    def __init__(self, path: Path, root: str = "Item"):
        """
        Initializes the XMLReader with the file path and the name of the root element.

        Args:
            path (Path): Path to the XML file to be read.
            root (str): Name of the XML element containing individual data entries (default is "Item").
        """
        self.path: Path = path
        self.dic_header: dict[str, int] = {}
        self.tree_root: str = root
    
    def read(self) -> list[DataModel]:
        """
        Parses the XML file and converts its content into a list of DataModel objects.

        Returns:
            list[DataModel]: A list of DataModel objects created from the XML data.

        """
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
        """
        Returns the headers of the XML file as a dictionary.

        Returns:
            dict[str, int]: A dictionary where keys are element tags and values are their indices.
        """
        return self.dic_header