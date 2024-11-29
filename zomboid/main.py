from pathlib import Path
from src import Zomboid
from src.context import Context
from src.paginator import Paginator
from src.data_utils import DataUtils

if __name__ == "__main__":
    paths = Path("zomboid/.data/model.csv")
    context = Context(paths)
    reader = context.get_reader()
    data_model = reader.read()
    separator = Paginator(source_models=data_model, skip=0, take=len(data_model))
    models = separator.get_models()
    result = DataUtils.find_item_by_name("Screwdriver", models)
    print(result)
    reader = Zomboid(models)
    reader.print_models()
