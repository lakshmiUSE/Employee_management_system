
import pytest

from employee_service import (
    add_employee,
    search_employees,
    update_employee,
    delete_employee
)
from exceptions import ValidationError, DuplicateEmployeeError


def test_add_employee():
    employee = {
        "name": "Rajesh",
        "email": "rameh1283@email.com",
        "department": "IT",
        "salary": "25000",
        "joining_date": "2026-10-15",
        "status": "Active"
    }

    assert add_employee(employee)

   # assert result["name"] == "Rajesh"
   # assert result["email"] == "rajesh@email.com"


def test_duplicate_email():
    employee = {
        "name": "Rajesh",
        "email": "rajesh9123gmail.com",
        "department": "IT",
        "salary": 25000,
        "joining_date": "2026-10-15",
        "status": "Active"
    }

    add_employee(employee)

    with pytest.raises(DuplicateEmployeeError):
        add_employee(employee)

def test_update_employee():
    employee = add_employee({
        "name": "Rajesh",
        "email": "sirisha93@gmail.com",
        "department": "IT",
        "salary": "25000",
        "joining_date": "2026-10-15",
        "status": "Active"
    })

    employee_id = employee["employee_id"]

    update_employee(employee_id, {"salary": "30000"})

    updated = search_employees("Rajesh")

    assert updated[0]["salary"] == 30000


def test_delete_employee():
    assert search_employees("Rajesh")
    employee = add_employee({
        "name": "Rajesh",
        "email": "rajaaaa022@gmail.com",
        "department": "IT",
        "salary": "25000",
        "joining_date": "2026-10-15",
        "status": "Active"

    })

    employee_id = employee["employee_id"]

    delete_employee(employee_id)