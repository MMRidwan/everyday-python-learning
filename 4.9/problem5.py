# Problem 5 — Password Strength Checker
# Question

# Given a password:

# Length ≥ 8
# Contains at least one digit
# Contains at least one uppercase letter

# Print:

# "Strong" or "Weak"

password = input("Enter password : ")

hasEightNumber = len(password) >= 8

hasOneDigit = False
hasOneUpper = False

for i in password :
    if i.isdigit() :
        hasOneDigit = True
    if i.isupper() :
        hasOneUpper = True
    
strong = (hasEightNumber and hasOneDigit and hasOneUpper)

print("Strong" if strong else "Weak")

# Expert

# is_strong = (
#     len(password) >= 8
#     and any(c.isdigit() for c in password)
#     and any(c.isupper() for c in password)
# )

# print("Strong" if is_strong else "Weak")
