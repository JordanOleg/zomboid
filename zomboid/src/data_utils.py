from src.model import DataModel

class DataUtils:
    @staticmethod
    def get_item_by_id(item_id: int, data_models: list[DataModel]) -> DataModel:
        """
        Finds and returns a DataModel object by its ID.

        Args:
            item_id (int): The ID of the item to find.
            data_models (list[DataModel]): A list of DataModel objects to search within.

        Returns:
            DataModel: The DataModel object with the given ID.
            
        Raises:
            ValueError: If no item with the given ID is found.
        """
        for item in data_models:
            if item.id == item_id:
                return item
        raise ValueError(f"Item with ID {item_id} not found.")
    
    @staticmethod
    def find_item_by_name(item_name: str, data_models: list[DataModel]) -> DataModel:
        """
        Finds and returns a DataModel object by its name.

        Args:
            item_name (str): The name of the item to find.
            data_models (list[DataModel]): A list of DataModel objects to search within.

        Returns:
            DataModel: The DataModel object with the given name.
            
        Raises:
            ValueError: If no item with the given name is found.
        """
        for item in data_models:
            if item.name.lower() == item_name.lower():
                return item
        raise ValueError(f"Item with name '{item_name}' not found.")
