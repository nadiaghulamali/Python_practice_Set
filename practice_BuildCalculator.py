try:
    a = int(input("Enter the first number:"))
    b = int(input("Enter the first number:"))

    print("what operation do you want to perform. Press '+' for addition\nPress '-' for subtraction\npress '*' for multiplication\nPress '/' for divition" )

    operation = input("Enter operation: ")

    match operation : 
        case '+' :
            print(f"addition of numbers is:  {a+b}")
        case '-' :
            print(f"subtraction of numbers is:  {a-b}")
        case '*' :
            print(f"multiplication of numbers is:  {a*b}")
        case '/' :
            print(f"Division of numbers is:  {a/b}")
except Exception as e:
    print(e)
    

