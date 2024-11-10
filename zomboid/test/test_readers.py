from pathlib import Path
from zomboid.src.model import DataModel
from src.io.csv_reader import CSVReader
from src.io.json_reader import JSONReader
from src.io.xml_reader import XMLReader


current_model = DataModel(2, "Nails", "Fasteners", "Good", 450)

def test_csv_reader() -> None:
    paths = Path("C:/Users/jorda/Desktop/Zomboid/zomboid/.data/csv_model.csv")
    csv_reader = CSVReader(paths)
    models = csv_reader.read()
    data_model = models[1]
    assert current_model.name == data_model.name
    assert current_model.id == data_model.id
    
def test_json_reader() -> None:
    paths = Path("C:/Users/jorda/Desktop/Zomboid/zomboid/.data/json_model.json")
    json_reader = JSONReader(paths)
    models = json_reader.read()
    data_model = models[1]
    assert current_model.name == data_model.name
    assert current_model.id == data_model.id
    
def test_xml_reader() -> None:
    paths = Path("C:/Users/jorda/Desktop/Zomboid/zomboid/.data/xml_model.xml")
    xml_reader = XMLReader(paths)
    models = xml_reader.read()
    data_model = models[1]
    assert current_model.name == data_model.name
    assert current_model.id == data_model.id
    