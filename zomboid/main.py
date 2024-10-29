from pathlib import Path
from src.io import Zomboid, CSVReader

if __name__ == "__name__":
    paths = Path(".data\model.csv")
    reader = Zomboid(paths)
    