from rich.console import Console
from rich.table import Table
from src.io.model import DataModel


class ReaderModel:
    def __init__(self, data_model: list[DataModel], dic_data: dict[str, int],skip: int, take: int):
        self.data_model: list[DataModel] = data_model
        self.dic_data: dict[str, int] = dic_data
        self.skip: int = skip
        self.take: int = take
        self.str_models, self.modified_model = self._get_models()
    
    def print(self) -> None: # rich
        table = Table(title="Data Models")
        row_data: list[list[str]] = []
        list_head_models: list[str] = self.dic_data.keys()
        for head in list_head_models:
            table.add_column(head, justify="center", style="green", no_wrap=True)
        for model in self.modified_model:
            list_atribute_current_model = []
            for key in list_head_models:
                list_atribute_current_model.append(getattr(model, head, ""))
            row_data.append(list_atribute_current_model)
        for row in row_data:
            table.add_row(row, style="yellow")

        console = Console()
        console.print(table)
    
    def _get_models(self) -> tuple[str, list[DataModel]]:
        result = ""
        list_models = []
        skip_model = self.skip
        take_model = self.take
        for item in self.data_model:
            if skip_model != 0:
                skip_model -= 1
                continue
            if take_model != 0: 
                take_model -= 1
                list_models.append(item)
                result += self._str_models(item) + "; "
        return result, list_models

    def _str_models(self, model: DataModel) -> str:
        return f"DataModel: id={model.id}, name={model.name}, " \
               f"type={model.type_object}, condition={model.condition}, amount={model.amount}"

    def get_models(self) -> list[DataModel]:
        str_models, result = self._get_models()
        self.str_models = str_models
        self.str_models = result
        return result

    def __str__(self):
        #rich
        pass
