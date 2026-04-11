# Problem 6 — Number Classification
# Question

# Given a number:

# Positive even → "Positive Even"
# Positive odd → "Positive Odd"
# Negative → "Negative"
# Zero → "Zero"

number = int(input("What is the Number : "))
result = ""    
    
if number > 0 :
    if number % 2 == 0 :
        result = "Positive Even"
    else : 
        result = "Positive Odd"
elif number == 0 :
    result = "Zero"
else :
    result = "Negative"
    
print(result)
        
        
# Expert
# if num == 0:
#     result = "Zero"
# elif num < 0:
#     result = "Negative"
# else:
#     result = "Positive Even" if num % 2 == 0 else "Positive Odd"

# print(result)