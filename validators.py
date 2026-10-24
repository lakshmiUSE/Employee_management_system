import re
from exceptions import ValidationError
from config import ALLOWED_DEPARTMENTS, ALLOWED_STATUSES, DATE_FORMAT
from datetime import datetime
def validate_name(name):
    if not isinstance(name,str) or not name.strip():
     raise ValidationError("Full name is required")
    return name.strip()

def validate_email(email):
   if not isinstance(email,str):
      raise ValidationError("Email is required")
   email=email.strip()
   format = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
   if not re.fullmatch(format,email):
        raise ValidationError("Please enter a valid email address.")
   return email

def validate_salary(salary):
   if isinstance(salary,bool):
          raise ValidationError("Salary must be a positive number.")
   try :
          salary=float(salary)
   except (ValueError,TypeError):
       raise ValidationError("Salary must be a valid numbe")

   if salary <=0:
       raise ValidationError("Salary must be greater than zero")  
       
   return salary
def validate_department(department):
    if not  isinstance(department,str):
       raise ValidationError("deparment is required")

    department=department.strip()

    if department not in ALLOWED_DEPARTMENTS:
        raise ValidationError(
            f"Choose a department from: {', '.join(ALLOWED_DEPARTMENTS)}"
        )

    return department
def validate_joining_date(joining_date):
    if not isinstance (joining_date,str):
        raise ValidationError("Joining date must use YYYY-MM-DD")
    
    try:
        datetime.strptime(joining_date, DATE_FORMAT)
    except ValueError:
        raise ValidationError(
            "Invalid joining date. Use YYYY-MM-DD, for example 2026-10-15."
        )

    return joining_date

def validate_status(status):
    if not isinstance(status, str) or status not in ALLOWED_STATUSES:
        raise ValidationError("Status must be Active or Inactive.")
    return status


def  validate_employee_data(employee_data):
    if not isinstance(employee_data,dict):
        raise  ValidationError("Employee information must be a dictionary.")

    return{
          "name": validate_name(employee_data.get("name")),
        "email": validate_email(employee_data.get("email")),
        "department":validate_department(
            employee_data.get("department")
        ),
        "salary": validate_salary(employee_data.get("salary")),
        "joining_date": validate_joining_date(
            employee_data.get("joining_date")
        ),
        "status":validate_status(employee_data.get("status","Active"))
    }

"""
employee = {
    "name": input("Enter employee name: "),
    "email": input("Enter employee email: "),
    "department": input("Enter department: "),
    "salary": input("Enter salary: "),
    "joining_date": input("Enter joining date (YYYY-MM-DD): "),
    "status": input("Enter status (Active/Inactive): ")
}


result = validate_employee_data(employee)
print("Employee details are valid:")
print(result)
"""