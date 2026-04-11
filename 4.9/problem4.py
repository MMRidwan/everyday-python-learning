# Problem 4 — Transaction Fee Logic
# Question

# Given an amount:

# < 100 → fee = 2%
# 100–500 → fee = 5%

# 500 → fee = 10%

# Print final amount after fee deduction.

amount = float(input("Enter your amount : "))

fee = 0

if amount < 100 :
    amount = amount - (amount * .02)
elif 100 <= amount <= 500 :
    amount = amount - (amount * .05)
elif amount >= 500 :
    amount = amount - (amount * .1)
else :
    amount = amount
    
print(str(amount))


# Expert
# def calculate_final(amount):
#     if amount < 100:
#         rate = 0.02
#     elif amount <= 500:
#         rate = 0.05
#     else:
#         rate = 0.10
#     return amount * (1 - rate)

# print(calculate_final(amount))