print("--- Python OOP Project : Employee Management System ---")
person=None
employee=None
manager=None
while True :
     print()
     print("Choose an operation :")
     print("1. Create a Person ")
     print("2. Create an Employee ")
     print("3. Create a Manager ")
     print("4. Show Details ")
     print("5. Exit")
     choice=int(input("Enter your choice :"))

     match choice:

        case 1:
             class Person : 
                def __init__(self):
                    self.Name=input("\nEnter Name : ")
                    self.Age=int(input("Enter Age : "))
                def display(self):
                    print("\nPerson Detail :")
                    print("Name :",self.Name)
                    print("Age :",self.Age)

             person1=Person()

             print(f"\nPerson created with name : {person1.Name} and age : {person1.Age} .\n")

             print("--- Choose another operation ---")
        
        case 2:
              class Employee:
                  def __init__(self):
                    self.Name=input("\nEnter Name :")
                    self.Age=int(input("Enter Age : "))
                    self.__Employee_Id=input("Enter Employee ID : ")
                    self.__Salary=int(input("Enter Salary : "))

                  def get_employee_id(self):
                    return self.__Employee_Id

                  def set_employee_id(self, Employee_Id):
                    self.__Employee_Id = Employee_Id

                  def get_salary(self):
                    return self.__Salary
                  
                  def set_salary(self, Salary):
                    self.__Salary = Salary
                  def display(self):
                    print("\nEmployee Detail :")
                    print("Name :",self.Name)
                    print("Age :",self.Age)
                    print("Employee_Id :",self.get_employee_id())
                    print("Salary :$",self.get_salary())

              employee=Employee()
              print(f"\nEmployee created with name: {employee.Name}, Age: {employee.Age} ,ID: {employee.get_employee_id()} and salary: ${employee.get_salary()} .")

              print("\n--- Choose another operation ---")

        case 3:
              class Manager(Employee):
                  def __init__(self):
                    super().__init__()
                    self.Department=input("Enter Department : ")
                  def display(self):
                    print("\nManager Detail :")
                    print("Name :",self.Name)
                    print("Age :",self.Age)
                    print("Employee_Id :",self.get_employee_id())
                    print("Salary :$",self.get_salary())
                    print("Department :",self.Department)

              manager=Manager()

              print(f"\nManager created with name: {manager.Name}, Age: {manager.Age}, ID: {manager.get_employee_id()}, salary: ${manager.get_salary()} and department: {manager.Department}.")

              print("\n--- Choose another operation ---")

        case 4: 
             print("\nchoose details to show :")

             print("1. Person")
             print("2. Employee")
             print("3. Manager")
             choose=int(input("Enter your choice : "))

             match choose :
                 case 1 :
                     if (person1 is not None):
                         person1.display()
                     else:
                         print("First create Person ")
                 case 2 :
                     if (employee is not None):
                         employee.display()
                     else:
                         print("First create employee ") 
                 case 3 :
                     if (manager is not None):
                         manager.display()
                     else:
                         print("First create manager")  
                 case _:
                     print("inavlid choose")
        case 5 :
             print("\nExiting the system. All resources have been freed.\n\nGoodbye!")
             break
        case _:
             print("Invalid choice")
             
                         