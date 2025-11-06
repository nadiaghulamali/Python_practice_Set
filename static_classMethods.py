'''✅ What are Getters and Setters?

In Python, getters and setters are used to:
✔ Access (get) the value of a private variable
✔ Update (set) the value of a private variable
'''

class Employee:
    def __init__(self, salary):
        self.__salary = salary

    # Getter method
    @property
    def salary(self):
        return self.__salary
    
    # Setter method
    @salary.setter
    def salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary!")

    @staticmethod
    def sum(a,b):
        return a+b


emp = Employee(50000)
print(emp.salary)    #  No brackets needed (getter)

emp.salary = 60000   #  Uses setter
print(emp.salary)

#instance and static methods 

'''
a method inside the class is an instance method and it takes self as argument 
 def sum (self,a,b)
   return a+b

   no need of self -> when no need slef , use static method it doesnt need self 

   | Use Case                    | Why Static Method?                                                  |
| --------------------------- | ------------------------------------------------------------------- |
| Utility/helper functions    | When a method performs a task but doesn’t need object or class data |
| Organize code inside class  | Keeps related logic together inside the class                       |
| No need to create an object | Can be called directly using class name                             |

'''


class Math:
    @staticmethod
    def add(a, b):
        return a + b

# No object creation
print(Math.add(5, 3))   #  works directly with class name


'''

A class method is a method that belongs to the class itself, not to a specific object (instance).

You define it using the decorator:

@classmethod


It automatically receives the class (not the object) as its first argument — conventionally called cls.

'''

class Employee:
    company = "google"

    @classmethod
    def change_Company(cls,company_name):
      cls.company = company_name


emp = Employee()

print(emp.company)
Employee.change_Company("Microsoft")
print(emp.company)


a= 10
b = 0

try: 
    c = a/b 
    print(c)
except Exception as e:
    print(e)
finally:
    print("this will always executed") #will be executed even with or without exception It's mainly used for cleanup actions, like closing files, disconnecting from databases, releasing resources, etc.
