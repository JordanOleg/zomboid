from src.io.model import DataModel


class SeparatorModel:
    def __init__(self, source_models: list[DataModel], skip: int, take: int):
        self.data_models: list[DataModel] = source_models
        self.skip: int = skip
        self.take: int = take
    
    def get_models(self) -> list[DataModel]:
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
        return list_models