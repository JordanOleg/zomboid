from src.model import DataModel


class Paginator:
    """
    A class that provides pagination functionality for a list of DataModel objects.

    Attributes:
        data_models (list[DataModel]): The source list of DataModel objects to paginate.
        skip (int): The number of items to skip before starting pagination.
        take (int): The number of items to include in the paginated result.
    """
    def __init__(self, source_models: list[DataModel], skip: int, take: int):
        """
        Initializes the Paginator with the source data, number of items to skip, and number of items to take.

        Args:
            source_models (list[DataModel]): The list of DataModel objects to paginate.
            skip (int): The number of items to skip before starting pagination.
            take (int): The number of items to take for the paginated result.
        """
        self.data_models: list[DataModel] = source_models
        self.skip: int = skip
        self.take: int = take
    
    def get_models(self) -> list[DataModel]:
        """
        Retrieves the paginated list of DataModel objects based on the skip and take values.

        Returns:
            list[DataModel]: A list containing the paginated DataModel objects.
        """
        list_models = []
        skip_model = self.skip
        take_model = self.take
        for item in self.data_models:
            if skip_model != 0:
                skip_model -= 1
                continue
            if take_model != 0: 
                take_model -= 1
                list_models.append(item)
        return list_models