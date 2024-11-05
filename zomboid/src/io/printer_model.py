from rich.console import Console
from rich.table import Table
from src.io.model import DataModel, get_dict_data_models


class PrinterModel:
    def __init__(self, data_model: list[DataModel], heads_table: dict[str, int] = None):
        self.data_model: list[DataModel] = data_model
        self.heads_table: dict[str, int] = heads_table if heads_table != None else get_dict_data_models()
    
    def print(self) -> None: # rich
        table = Table(title="Data Models")
        row_data: list[list[str]] = []
        list_atribute_current_model = []
        list_head_models: list[str] = self.heads_table.keys()
        for head in list_head_models:
            table.add_column(head, justify="center", style="green", no_wrap=True)
        for model in self.data_model:
            for head in list_head_models:
                list_atribute_current_model.append(getattr(model, head, ""))
            row_data.append(list_atribute_current_model)
        for row in row_data:
            table.add_row(*row, style="yellow")

        console = Console()
        console.print(table)
