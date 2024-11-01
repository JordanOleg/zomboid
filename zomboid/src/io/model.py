from dataclasses import dataclass


@dataclass
class DataModel:
    id: str
    name: str
    type_object: str
    condition: str
    amount: str

def get_dict_data_models() -> dict[str, int]:
    return {
        "id" : 0,
        "name" : 1,
        "type_object" : 2,
        "condition" : 3,
        "amount" : 4
    }