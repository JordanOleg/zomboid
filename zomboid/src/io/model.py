from dataclasses import dataclass


@dataclass
class DataModel:
    id: str
    name: str
    type_object: str
    condition: str
    amount: str
