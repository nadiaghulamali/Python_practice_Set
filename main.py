print("hello world",6);
# a = input("Enter something: ");
# print(a);
# print("Goodbye!\n \"okay\"");
# food = input("What is your favorite food? ");
# print("Your favorite food is " + food);

# Strings

# name = "Nadia"
# print(name[3], name[-3],name[0:3], name[1:], name[:4]);
# print(name[-2 + len(name)])
# print(name[2:-1])#same
# print(name[2: len(name)-1]) #staticmethod
# print(name[2: 4])   
# 
# 
# a = "aeiwo orvh aieouu sdgh"
# print(a.count("a","i","o","e","u"))

# a = "aeiwo orvh aieouu sdgh"
# vowels = "aeiou"
# count = sum(a.count(v) for v in vowels)
# print(count)

# s = "imanami"
# s2 = s[::-1] 
# if  s == s2:
#     print("palindrome")
# else:
#     print("not palindrome")


# a = "aeiwo orvh aieouu sdgh"
# vowels = "aeiou"
# sum = 0

# for char in a :
#     if char in vowels:
#         sum +=1

# print("Number of vowels:", sum)


# def fib(n):
#     if(n==0 or n==1):
#         return n
#     return fib(n-2) + fib(n-1)

# print(fib(6))

# def factorial(n):
#     if(n<=2)
#         return n
#     return n * factorial(n-1)

def sum_to_n(n):
    if(n==0):
        return 0
    
    return n%10 + sum_to_n(n//10)


print(sum_to_n(5))