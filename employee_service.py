from validators import validate_employee_data
from exceptions import (
    EmployeeNotFoundError,
    DuplicateEmployeeError,
    ValidationError
)
import uuid
import repository
def add_employee(employee_data):
    employee=validate_employee_data(employee_data)
    employees=repository.load_employees()

    for emp in employees:
        if emp["email"].lower()==employee["email"].lower():
             raise DuplicateEmployeeError("Email already exists")

    employee["employee_id"] = str(uuid.uuid4())
    repository.insert_employee(employee)
    return employee

def get_all_employees():
    return repository.load_employees()

def get_employee_by_id(employee_id):
    employee = repository.find_employee_by_id(employee_id)

    if employee is None:
        raise EmployeeNotFoundError("Employee not found")

    return employee

def search_employees(search_term):
    employees = repository.load_employees()
    result = []

    for emp in employees:
        if search_term.lower() in emp["name"].lower():
            result.append(emp)
            return result
        
        return "Employee not found"
def update_employee(employee_id,updated_data):
    employee=get_employee_by_id(employee_id)
    if not isinstance(updated_data, dict):
        raise ValidationError("Data must be a dictionary")
     
    employee.update(updated_data)
    employee = validate_employee_data(employee)

    employees = repository.load_employees()

    for emp in employees:
        if (
            emp["employee_id"] != employee_id
            and emp["email"].lower() == employee["email"].lower()
        ):
            raise DuplicateEmployeeError("Email already exists")

    repository.update_employee_record(employee_id, employee)
    return employee

def delete_employee(employee_id):
    if not repository.delete_employee_record(employee_id):
        raise EmployeeNotFoundError("Employee not found")

    return "Employee deleted successfully"

def filter_employees(filters):
    employees = repository.load_employees()

    department = filters.get("department")
    status = filters.get("status")
    result = []

    for emp in employees:
        if department and emp["department"].lower() != department.lower():
           continue

        if status and emp.get("status", "Active").lower !=status.lower():
            continue

        result.append(emp)

    return result

