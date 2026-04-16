# Problem 1
# easy
# Print 1 to 100
# Print every integer from 1 to 100, each on its own line. Simple — but the point is getting range exactly right. Off by one and you fail silently.

# def print_integer(number) :
#     for counter in range(1, number, 1) :
#         print(counter, counter + 1)
        
# print_integer(5)

def print_integer(number) :
    for counter in range(1, number+1, 1) :
        print(counter)
        
print_integer(5)
        

# Problem 2
# easy
# Sum 1 to 1000
# Calculate and print the sum of every integer from 1 to 1000. Do not use Python's built-in sum(). 
# The interviewer wants to see you accumulate a value across iterations manually. 

def print_sum(number) :
    result = 0
    for counter in range(1, number+1, 1) :
        result = result + counter
    print(result) 
       
print_sum(1000)