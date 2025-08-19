import sys
employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Div', 'age': 24, 'department': 'IT', 'salary': 38000},
    103: {'name': 'Aman', 'age': 25, 'department': 'Finance', 'salary': 250000}
}

def add_employee():
    while True:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists! Please enter a unique ID.")
        else:
            break

    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = float(input("Enter Employee Salary: "))

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }
    print("Employee added successfully!\n")


def view_employees():
    if not employees:
        print("No employees available.")
        return

    print("\n--- Employee Records ---")
    print(f"{'ID':<6} {'Name':<15} {'Age':<5} {'Department':<12} {'Salary':<10}")
    print("-" * 50)
    for emp_id, details in employees.items():
        print(f"{emp_id:<6} {details['name']:<15} {details['age']:<5} {details['department']:<12} {details['salary']:<10}")
    print()


def search_employee():
    emp_id = int(input("Enter Employee ID to search: "))
    if emp_id in employees:
        emp = employees[emp_id]
        print("\n--- Employee Found ---")
        print(f"ID: {emp_id}")
        print(f"Name: {emp['name']}")
        print(f"Age: {emp['age']}")
        print(f"Department: {emp['department']}")
        print(f"Salary: {emp['salary']}")
    else:
        print("Employee not found.\n")


def main_menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("Thank you for using the Employee Management System!")
            sys.exit()
        else:
            print("Invalid choice, please try again.\n")


main_menu()