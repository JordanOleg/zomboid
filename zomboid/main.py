from pathlib import Path
from src.io import Zomboid
from src.io.csv_reader import CSVReader
from src.io.json_reader import JSONReader
from src.io.separator_model import SeparatorModel

if __name__ == "__main__":
    paths = Path("C:/Users/jorda/Desktop/Zomboid/zomboid/.data/json_model.json")
    reader = JSONReader(paths)
    data_model = reader.read()
    print(data_model)
    separator = SeparatorModel(source_models=data_model, skip=2, take=4)
    models = separator.get_models()
    reader = Zomboid(models) # Zomboid(models, reader.get_header())
    reader.print_models()
