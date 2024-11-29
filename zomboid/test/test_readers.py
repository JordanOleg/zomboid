import pytest
import tempfile
import json
import os
from src.io.csv_reader import CSVReader
from src.io.json_reader import JSONReader
from src.io.xml_reader import XMLReader
from src.model import DataModel

@pytest.fixture
def csv_file():
    csv_content = """id,name,type_object,condition,amount
1,Hummer,Tool,Mint,10
2,Nails,Fasteners,Good,450
3,Nails,Fasteners,Bad,100
"""
    temp_file = tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".csv")
    try:
        temp_file.write(csv_content)
        temp_file.seek(0)
        yield temp_file.name
    finally:
        temp_file.close()
        os.unlink(temp_file.name) 

@pytest.fixture
def json_file():
    json_content = """[
    {
        "id": 1,
        "name": "Hummer",
        "type_object": "Tool",
        "condition": "Mint",
        "amount": 10
    },
    {
        "id": 2,
        "name": "Nails",
        "type_object": "Fasteners",
        "condition": "Good",
        "amount": 450
    },
    {
        "id": 3,
        "name": "Nails",
        "type_object": "Fasteners",
        "condition": "Bad",
        "amount": 100
    }
]"""
    temp_file = tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".json")
    try:
        temp_file.write(json_content)
        temp_file.seek(0)
        yield temp_file.name
    finally:
        temp_file.close()
        os.unlink(temp_file.name) 

@pytest.fixture
def xml_file():
    xml_content = """<items>
    <Item>
        <id>1</id>
        <name>Hummer</name>
        <type_object>Tool</type_object>
        <condition>Mint</condition>
        <amount>10</amount>
    </Item>
    <Item>
        <id>2</id>
        <name>Nails</name>
        <type_object>Fasteners</type_object>
        <condition>Good</condition>
        <amount>450</amount>
    </Item>
    <Item>
        <id>3</id>
        <name>Nails</name>
        <type_object>Fasteners</type_object>
        <condition>Bad</condition>
        <amount>100</amount>
    </Item>
</items>
"""
    temp_file = tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".xml")
    try:
        temp_file.write(xml_content)
        temp_file.seek(0)
        yield temp_file.name
    finally:
        temp_file.close()
        os.unlink(temp_file.name)
    

current_model = DataModel(2, "Nails", "Fasteners", "Good", 450)

def test_csv_reader(csv_file) -> None:
    csv_reader = CSVReader(csv_file)
    models = csv_reader.read()
    data_model = models[1]
    assert current_model.name == data_model.name
    assert current_model.id == data_model.id
    
def test_json_reader(json_file) -> None:
    json_reader = JSONReader(json_file)
    models = json_reader.read()
    data_model = models[1]
    assert current_model.name == data_model.name
    assert current_model.id == data_model.id
    
def test_xml_reader(xml_file) -> None:
    xml_reader = XMLReader(xml_file)
    models = xml_reader.read()
    data_model = models[1]
    assert current_model.name == data_model.name
    assert current_model.id == data_model.id
    