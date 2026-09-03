# What does int("42") return? What does int("42.0") return?
print(int("42")) # 42

print(int("42.0")) # since its a floating number in a string format it would be error, if it was directly a floating then it wwould just truncate the floating portion

# What does bool("False") evaluate to, and why does that surprise almost everyone the first time?
print(bool("False")) # True, because it says false but the string is non-empty so its truthy

# Predict the output: print(int(-7.8))
print(int(-7.8)) # -7

# You write age = input("Age: ") and the user types 30. What is the type of age right now, and what happens if you immediately do age + 1?
age = input("Age : " ) # Age is string
print(f"{age + 1}") # fails because age is a string and cant do string + int

print(f"{int(age) + 1}") # passes because coverting to int first