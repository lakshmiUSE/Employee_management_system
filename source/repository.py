
import json
from config.config import DATA_FILE
from .exceptions import DataStorageError




def load_employees():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            if not file.read().strip():
                return []

            file.seek(0)
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError as e:
        raise DataStorageError("Invalid JSON data") from e

    except OSError as e:
        raise DataStorageError("Unable to read employee data") from e


def save_employees(employees):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(employees, file, indent=4)
    except OSError as e:
        raise DataStorageError("Unable to save employee data") from e


def insert_employee(employee):
    employees = load_employees()
    employees.append(employee)
    save_employees(employees)
