# for i in range(len(fruits)):
#     print(i, fruits[i])


# is same as

fruits = ["apple", "mango", "pear"]

# for fruit in enumerate(fruits):
#     print(fruit)


# for fruit, counter, ehat in enumerate(fruits):
#     print(fruit, counter)
    
counter = 0

for fruit in fruits :
    print(counter, fruit)
    counter+=1
    