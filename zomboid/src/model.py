from dataclasses import dataclass


@dataclass
class DataModel:
    """
    A data representation class used for serialization and deserialization of data 
    within the project.

    Attributes:
        id (str): A unique identifier for the data model.
        name (str): The name or title of the data model.
        type_object (str): The type or category of the object represented by the data model.
        condition (str): A description of the current state or condition of the object.
        amount (str): A quantity or numerical value associated with the object.
    """
    id: str
    name: str
    type_object: str
    condition: str
    amount: str

default_dict_models: dict[str, int] = {
    "id" : 0,
    "name" : 1,
    "type_object" : 2,
    "condition" : 3,
    "amount" : 4
}