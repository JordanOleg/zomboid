from pathlib import Path
from src.io import Zomboid
from src.io.csv_reader import CSVReader
from src.io.separator_model import SeparatorModel

if __name__ == "__name__":
    paths = Path("zomboid/.data/model.csv")
    reader = CSVReader(paths)
    data_model = reader.read()
    separator = SeparatorModel(source_models=data_model, skip=2, take=4)
    models = separator.get_models()
    reader = Zomboid(models) # Zomboid(models, reader.get_header())
    reader.print_models()
