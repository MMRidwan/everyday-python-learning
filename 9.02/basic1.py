# Write an if/elif/else chain from memory that classifies a number as negative, zero, or positive.

# Separately, explain out loud — no notes — why if []: does not execute its body.

number = float(input("Give me a number : "))

if number > 0 :
    print(f"{number} is positve")
elif number < 0 :
    print(f"{number} is negative")
else :
    print(f"{number : .0f} is ZERO")