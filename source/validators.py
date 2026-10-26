from .exceptions import ValidationError
from config.config import ALLOWED_DEPARTMENTS, ALLOWED_STATUSES, DATE_FORMAT
from datetime import datetime
import re
def validate_name(name):
    if not isinstance(name,str) or not name.strip():
      raise ValidationError("Full name is requried")
    return name.strip() 

def validate_email(email):
   if not isinstance(email,str) or not email.strip():
        raise ValidationError(" email is requried")
   
   email= email.strip()
   pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

   if not re.fullmatch(pattern,email):
       raise ValidationError("Please enter a valid email address")
   
   return email

def validate_salary(salary):
    if  isinstance(salary,bool):
        raise ValidationError("salary must be valid number")
    

    try:
        salary = float(salary)
    except (ValueError, TypeError):
        raise ValidationError("Salary must be a valid number.")

    if salary <= 0:
        raise ValidationError("Salary must be greater than zero.")

    return salary

def validate_department(department):
    if not isinstance(department,str) or not department.strip():
        raise ValidationError("Department is required")

    department = department.strip()

    if department not in ALLOWED_DEPARTMENTS:
        raise ValidationError(
            f"Choose a department from: {', '.join(ALLOWED_DEPARTMENTS)}"
        )

    return department

def validate_joining_date(joining_data):
    if not isinstance(joining_data,str) or not joining_data.strip():
        raise ValidationError("Joining date is required. Use YYYY-MM-DD")

    try:
         data=datetime.strptime(joining_data,DATE_FORMAT)

         if data.strftime(DATE_FORMAT)!=joining_data:
             raise ValueError
    except ValueError:
        raise  ValidationError(" Invalid joining date. Use YYYY-MM-DD, for example 2026-10-15")

    return joining_data


def validate_status(status):
    if not isinstance(status, str) or status not in ALLOWED_STATUSES:
        raise ValidationError("Status must be Active or Inactive.")

    return status

def validate_employee_data(employee_data):
    if not isinstance(employee_data, dict):
        raise ValidationError("Employee information must be a dictionary.")

    return {
        "name": validate_name(employee_data.get("name")),
        "email": validate_email(employee_data.get("email")),
        "department": validate_department(employee_data.get("department")),
        "salary": validate_salary(employee_data.get("salary")),
        "joining_date": validate_joining_date(
            employee_data.get("joining_date")
        ),
        "status": validate_status(employee_data.get("status", "Active"))
    }

          
        