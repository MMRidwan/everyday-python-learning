#“From memory, write a script that reads two numbers via input(), converts them safely, and prints a formatted f-string sentence using the result. 
x = int(input("What is your age: "))
y = float(input("How much money do you have : "))

print(f"{x} is your age {y} is how much you have and {x + y} is your toal")
# State out loud why int("3.5") raises a ValueError before you test it.”
# int can only convert a string with integer value, not one with floating or anything non-int type