from pathlib import Path
from src import Zomboid
from src.context import Context
from src.paginator import Paginator

if __name__ == "__main__":
    paths = Path("zomboid/.data/model.json")
    context = Context(paths)
    reader = context.get_reader()
    data_model = reader.read()
    separator = Paginator(source_models=data_model, skip=0, take=4)
    models = separator.get_models()
    reader = Zomboid(models)
    reader.print_models()
