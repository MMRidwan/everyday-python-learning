
favorite_fruit = "blueberry"

length = len(favorite_fruit)

last_chars = favorite_fruit[length-4:]
print(last_chars)
# Output: erry


first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name) :
  new_first = first_name[-3 :]
  new_last = last_name[-3 :]
  temp_password = new_first + new_last
  return temp_password

temp_password = password_generator(first_name, last_name)
print(temp_password)
