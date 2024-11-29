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
    
    @staticmethod
    def get_percentage_by_condition(data_models: list[DataModel]) -> dict[str, float]:
        """
        Calculates the percentage of each condition across all items.

        Args:
            data_models (list[DataModel]): A list of DataModel objects.

        Returns:
            dict[str, float]: A dictionary where keys are conditions (Mint, Good, etc.)
                              and values are the percentage of items with that condition.
        """
        total_items = len(data_models)
        condition_counts = {"Mint": 0, "Good": 0, "Average": 0, "Bad": 0}
        
        for item in data_models:
            if item.condition in condition_counts:
                condition_counts[item.condition] += 1
        
        condition_percentages = {condition: (count / total_items) * 100
                                 for condition, count in condition_counts.items()}
        
        return condition_percentages
    
    @staticmethod
    def get_percentage_by_condition_and_name(item_name: str, data_models: list[DataModel]) -> dict[str, float]:
        """
        Calculates the percentage of each condition for items with a specific name.

        Args:
            item_name (str): The name of the items to filter.
            data_models (list[DataModel]): A list of DataModel objects.

        Returns:
            dict[str, float]: A dictionary where keys are conditions (Mint, Good, etc.)
                              and values are the percentage of items with that condition and name.
        """
        filtered_items = [item for item in data_models if item.name.lower() == item_name.lower()]
        return DataUtils.get_percentage_by_condition(filtered_items)
