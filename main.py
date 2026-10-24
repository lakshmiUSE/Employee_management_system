from exceptions import ValidationError
import employee_service 
def display_menu():
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Filter Employees")
    print("7. Exit")
display_menu()
choice=input("Enter your choice:")

if choice == "1":
     data = {
                "name": input("Enter name: "),
                "email": input("Enter email: "),
                "department": input("Enter department: "),
                "salary": float(input("Enter salary: ")),
                "joining_date": input("Enter joining date (YYYY-MM-DD): "),
                "status": input("Enter status: ")
                
    }
     try:
        employee=employee_service.add_employee(data)
        print(employee)
     except ValidationError as e:
         print(e)    
         
elif choice == "2":
     employees = employee_service.get_all_employees()
     print(employees)


elif choice == "3":
    search = input("Enter employee name: ")
    result = employee_service.search_employees(search)
    print(result)         

elif choice =="4":
     employee_id=input("Enter employee name: ")
     data = {
            "name": input("Enter updated name: "),
            "email": input("Enter updated email: "),
            "department": input("Enter updated department: "),
            "salary": float(input("Enter updated salary: ")),
            "joining_date": input("Enter updated joining date: "),
            "status": input("Enter updated status: ")
        }

     result = employee_service.update_employee(employee_id, data)
     print(result)

elif choice == "5":
        employee_id = input("Enter employee ID:")
        result = employee_service.delete_employee(employee_id)
        print(result)
    
elif choice == "6":
        department = input("Enter department to filter: ")
        result = employee_service.filter_employees(department)
        print(result)

elif choice == "7":
        print("Exiting Employee Management System.")
         

else:
        print("Invalid choice. Please try again.")
