import json 

File="employee.json"

def load_employees():
    try :
        with open(File,"r")as file:
            employees=json.load(file)
          
        if not employees:
            return ["Employee not found"]

        return employees

    except FileNotFoundError:
        return ["Employee not found"]
def save_employees(employees):
    with open(File,"w")as file:
        json.dump(employees,file,indent=4)
    
def find_employee_by_id(employee_id):
    employees = load_employees()

    for employee in employees:
        if employee["employee_id"] == employee_id:
            return employee

    return None


def insert_employee(employee):
    employees = load_employees()
    employees.append(employee)
    save_employees(employees)

def update_employee_record(employee_id, employee):
    employees = load_employees()

    for emp in employees:
        if emp["employee_id"] == employee_id:
            emp.update(employee)
            save_employees(employees)
            return True
        
    return False

def delete_employee_record(employee_id):
    employees = load_employees()

    for emp in employees:
        if emp["employee_id"] == employee_id:
            employees.remove(emp)
            save_employees(employees)
            return True

    return False


"""
employee  = {
    "employee_id": 101,
    "full_name": "Ravi",
    "department": "IT",
    "salary": 30000
}

insert_employee(employee)

print(find_employee_by_id(101))

print(update_employee_record(101, {"salary": 40000}))

delete_employee_record(101)

"""