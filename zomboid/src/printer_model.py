from rich.console import Console
from rich.table import Table
from src.model import DataModel, default_dict_models


class PrinterModel:
    """
    A class for rendering a list of DataModel objects as a formatted table using the Rich library.

    Attributes:
        data_model (list[DataModel]): A list of DataModel objects to display in the table.
        heads_table (dict[str, int]): A dictionary where keys represent column names and values
                                      indicate column ordering or priority.
                                      Defaults to a predefined dictionary if not provided.
    """
    def __init__(self, data_model: list[DataModel], heads_table: dict[str, int] = None):
        """
        Initializes the PrinterModel with the data to be displayed and table headers.

        Args:
            data_model (list[DataModel]): The list of DataModel objects to render in the table.
            heads_table (dict[str, int], optional): A dictionary of headers for the table. Defaults to `default_dict_models`.
        """
        self.data_model: list[DataModel] = data_model
        self.heads_table: dict[str, int] = heads_table if heads_table else default_dict_models
    
    def print(self) -> None: # rich
        """
        Renders the DataModel objects as a Rich table with headers and rows.
        """
        table = Table(title="Data Models")
        row_data: list[list[str]] = []
        
        list_head_models: list[str] = self.heads_table.keys()
        for head in list_head_models:
            table.add_column(head, justify="center", style="green", no_wrap=True)
        for model in self.data_model:
            list_attribute_current_model = []
            for head in list_head_models:
                list_attribute_current_model.append(str(getattr(model, head, "")))
            row_data.append(list_attribute_current_model)
        for row in row_data:
            table.add_row(*row, style="yellow")

        console = Console()
        console.print(table)
