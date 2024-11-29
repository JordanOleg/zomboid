import argparse
from pathlib import Path
from src import Zomboid
from src.context import Context
from src.paginator import Paginator
from src.data_utils import DataUtils


def cli_main() -> None:
    parser = argparse.ArgumentParser(description="Data model utilities.")
    parser.add_argument('--file', type=str, required=True, help="Path to the input file (CSV, JSON, or XML).")
    parser.add_argument('--percentage-all', action='store_true', help="Get percentage by condition for all items.")
    parser.add_argument('--percentage-name', type=str, help="Get percentage by condition for items with a specific name.")
    
    args = parser.parse_args()
    file_path = Path(args.file)

    if not file_path.exists():
        print(f"Error: File {file_path} does not exist.")
        return

    context = Context(file_path)
    data_models = context.get_model()

    if args.percentage_all:
        percentages = DataUtils.get_percentage_by_condition(data_models)
        print("Percentage by condition for all items:")
        for condition, percentage in percentages.items():
            print(f"{condition}: {percentage:.2f}%")

    if args.percentage_name:
        name = args.percentage_name
        percentages = DataUtils.get_percentage_by_condition_and_name(name, data_models)
        print(f"Percentage by condition for items with name '{name}':")
        for condition, percentage in percentages.items():
            print(f"{condition}: {percentage:.2f}%")


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
