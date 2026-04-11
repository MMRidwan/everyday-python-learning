# Problem 2
# medium
# Find the first duplicate
# Given a list of integers, find and return the first number that appears more than once. If no duplicate exists, return -1.
# find_first_duplicate([4, 3, 2, 7, 8, 2, 3, 1]) → 2 
# find_first_duplicate([1, 2, 3, 4]) → -1 
# find_first_duplicate([1, 1, 2]) → 1


numbers = [4, 3, 2, 7, 8, 2, 3, 1]

# def find_first_duplicate(numbers) :
#     for i in range(len(numbers)) :
#         for j in range(i+1, len(numbers)):
#             x = numbers[i]
#             y = numbers[j]
#             if numbers[i] == numbers[j] :
#                 print(numbers[i])
#                 break
    
# find_first_duplicate([4, 3, 2, 7, 8, 2, 3, 1])


# def find_first_duplicate(numbers) :
#     seen = []
#     for i in range(len(numbers)) :
#         seen.append(numbers[i])
#         if numbers[i+1] in seen :
#             return numbers[i+1]
#             break
#         else :
#             return -1


def find_first_duplicate(numbers) :
    seen = []
    for i in range(len(numbers)) :
        if numbers[i] in seen :
            return numbers[i]
        else :
            seen.append(numbers[i])
    return -1        
    
print(find_first_duplicate([4, 3, 2, 7, 8, 2, 3, 1]))
print(find_first_duplicate([1, 2, 3, 4]))
print(find_first_duplicate([1, 1, 2]))