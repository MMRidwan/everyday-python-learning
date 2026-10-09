# 1. 
a = "12"
b = 3
x = int(a) + b
y = a + str(b)
print(x, y) # 15, 123

# 2.
# n = int("3.5") crashes. Name the exact exception, then write the one-line expression that returns 3 from the string "3.5".
# ValueError

# 3.
# raw = input("Age: "). If it’s a valid whole number, print Age next year: N; otherwise print Invalid age. (Use try/except.)

raw = input("Age: ")
try:
    int(raw)
    print(f"Age next year is {int(raw) + 1}")
except(TypeError, ValueError, KeyError):
    print("Invalid Age")
    
# 4. 
# Meant to show "no items" only when there truly are no items, but a legitimate 0 triggers it too:
# count = 0
# display = count or "no items"
# print(display)

if(count is None or [] or "") :
    print("No Items")
else :
    print(display)
    
# 5. 
# Prints C for a 75; the intended answer is B:
score = 75
if score >= 90:
    grade = "A"
if score >= 70:
    grade = "B"
if score >= 50:
    grade = "C"
print(grade)

# Due to if being stacked, the last branch also runs and sets grade to C

# 6.
# Prints not empty for an empty list:
items = []
if items == None:
    print("empty")
else:
    print("not empty")
 
items = []
if(items == []):
     print("Empty")
else: 
    print("not empty")
