
import uuid
from .validators import validate_employee_data
from . import repository

from .exceptions import DuplicateEmployeeError

def add_employee(employee_data):
    employee=validate_employee_data(employee_data)
    employees=repository.load_employees()

    for emp in employees:
        if emp["email"].lower()==employee["email"].lower():
             raise DuplicateEmployeeError("Email already exists")

    employee["employee_id"] = str(uuid.uuid4())
    repository.insert_employee(employee)
    return employee
