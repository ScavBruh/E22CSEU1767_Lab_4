class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def _str_(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"

def sort_employee_data(employee_data, sort_key):
    if sort_key == 1:
        return sorted(employee_data, key=lambda emp: emp.age)
    elif sort_key == 2:
        return sorted(employee_data, key=lambda emp: emp.name)
    elif sort_key == 3:
        return sorted(employee_data, key=lambda emp: emp.salary)
    else:
        return employee_data

def main():
    employee_data = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000)
    ]

    print("Employee Table")
    print("{:<12} {:<10} {:<4} {:<14}".format("Employee ID", "Name", "Age", "Salary (PM)"))
    for employee in employee_data:
        print("{:<12} {:<10} {:<4} {:<14}".format(
            employee.emp_id,
            employee.name,
            employee.age,
            employee.salary
        ))

    while True:
        try:
            sort_option = int(input("Enter sorting parameter (1. Age, 2. Name, 3. Salary, 0. Quit): "))
            if sort_option == 0:
                break
            if sort_option not in (1, 2, 3):
                print("Invalid option. Please choose 1, 2, 3, or 0 to quit.")
                continue

            sorted_data = sort_employee_data(employee_data, sort_option)
            print("\nSorted Employee Table")
            print("{:<12} {:<10} {:<4} {:<14}".format("Employee ID", "Name", "Age", "Salary (PM)"))
            for employee in sorted_data:
                print("{:<12} {:<10} {:<4} {:<14}".format(
                    employee.emp_id,
                    employee.name,
                    employee.age,
                    employee.salary
                ))

        except ValueError:
            print("Invalid input. Please enter a valid sorting option.")

if __name__ == "_main_":
    main()