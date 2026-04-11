# Problem 2 — Username Validation
# Question

# Given a username string:

# Must be at least 5 characters
# Must not contain spaces
# Must start with a letter

# Print:

# "Valid" or "Invalid"
# Hints

result = ""
username = input("What is your user name : ")

if len(username) >= 5 and " " not in username and username[0].isalpha :
    result = "Valid"
else :
    result = "Invalid"
    
print(result)

# Expert
# is_valid = (
#     len(username) >= 5
#     and username[0].isalpha()
#     and " " not in username
# )

# print("Valid" if is_valid else "Invalid")