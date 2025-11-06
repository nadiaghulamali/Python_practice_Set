class Employee :
    company = "Google"
    name = "Nadia"
    age = "10"
    salary = 30000

    def __init__ (self, salary, name, age):
        self.salary = salary
        self.name = name
        self.age = age 

    def getSalary(self): #self -> object being reffered 
        return self.salary
    
    def __add__(self, other):
        return self.salary + other.salary

obj = Employee(34000,"Nadi",24)

print(obj.company) 
print(obj.name) 
print(obj.getSalary())

#constructors -> innitialize our objects 
#object introspect -> what methods and attributes has an object 

print(dir(obj))

#super -> call the parent class method 

class Animal:
    def speak(self):
        print("speaking now....")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("woof__") 

obj = Dog()
obj.speak()

#object overloading 



emp1 = Employee(30000,"Nadi",24)
emp2 = Employee(30000,"Nadia",34)

print(emp1 + emp2)

#decorater -> add extra functionality to existing function without making changes in that function 

'''
A decorator is just a way to add extra functionality to a function without changing its original code.

You can think of it like:

Wrapping a gift 🎁 (original function) with extra decoration 🎀 (extra functionality).

The gift remains the same, but now it's improved or more beautiful.

They are used when you want to:
✔ Add logging
✔ Add security checks
✔ Measure execution time
✔ Modify or extend a function’s behavior

And all that without touching the function’s actual code.

'''

def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                print(f"this code written by {a}")
                func(a)
                print(f"this code updated by {a}")
        return wrapper
    return decorator

@repeat(7)
def say_hello(a):
    print(f"say hello {a}")

say_hello("nadia")


