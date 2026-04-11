# Problem 1 — FizzBuzz Variant (With Priority Rules)
# Question

# Given an integer n, print:

# "FizzBuzz" if divisible by both 3 and 5
# "Fizz" if divisible by 3
# "Buzz" if divisible by 5
# Otherwise print the number
# Constraint

# You must handle priority correctly.

# Answer:
# n = int(input("Enter your number : "))

# if n % 3 == 0 and n % 5 == 0 :
#     print("FizzBuzz")
# elif n % 3 == 0 and n % 5 != 0 :
#     print("Fizz")
# elif n % 3 != 0 and n % 5 == 0 :
#     print("Buzz")
    
    
# Expert :
# result = ""

# if n % 3 == 0:
#     result += "Fizz"
# if n % 5 == 0:
#     result += "Buzz"

# print(result or n)

def FizzBuzz(n) :
    if n <= 0 :
        print("Cant be 0")
    elif n % 3 == 0 and n % 5 == 0 :
        print("FizzBuzz")
    elif n % 3 == 0 :
        print("Fizz")
    elif n % 5 == 0 :
        print("Buzz")
    else :
        print("Not Fizz or Buzz")
    
FizzBuzz(15)
FizzBuzz(5)
FizzBuzz(3)
FizzBuzz(7)
FizzBuzz(0)