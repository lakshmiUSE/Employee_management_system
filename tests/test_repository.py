import json
import pytest
from source import repository
def test_file_persistence(tmp_path):
    """Test saving and loading employee data from a file"""
    file_path = tmp_path / "emp_complete_data.json"

    employees = [
        {"employee_id": "101", "name": "Rajesh"}
    ]

    with open(file_path, "w") as file:
        json.dump(employees, file)

    with open(file_path, "r") as file:
        result = json.load(file)

    assert result == employees

def test_missing_file(tmp_path):
    """Test that a missing file does not exist."""
    file_path = tmp_path / "missing.json"

    assert not  file_path.exists()


def test_malformed_json():
    """Test that invalid json data rasie an error"""
    with pytest.raises(json.JSONDecodeError):
        json.loads("{invalid json")


def test_insert_employee():
    """Test inserting a new employee into the records""" 
    employee = {
        "employee_id": "101",
        "name": "Rajesh"
    }

    repository.save_employees([])
    repository.insert_employee(employee)

    assert employee in repository.load_employees()
