import json
import pytest



def test_file_persistence(tmp_path):
    file_path = tmp_path / "employees.json"

    employees = [
        {"employee_id": "101", "name": "Rajesh"}
    ]

    with open(file_path, "w") as file:
        json.dump(employees, file)

    with open(file_path, "r") as file:
        result = json.load(file)

    assert result == employees

def test_missing_file(tmp_path):
    file_path = tmp_path / "missing.json"

    assert not file_path.exists()


def test_malformed_json():
    with pytest.raises(json.JSONDecodeError):
        json.loads("{invalid json")

