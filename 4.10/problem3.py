# Reverse a string without using [::-1]
# Write a function that reverses a string using a loop. 
# You cannot use Python's built-in slice reversal [::-1] or reversed(). 
# The interviewer wants to see that you understand how iteration works, not just that you know a shortcut.

# reverse_string("hello") → "olleh" reverse_string("Python") → "nohtyP" reverse_string("a") → "a"

def ReverseString (string) :
    result = ""
    
    # range(index = 4, -1, -1)
    
    # Here, len(string)-1 = last index in a list
    # Explanation :
    # len(hello) = 5
    # len(string)-1 = 4
    
    # so start at index 4
    
    # "hello" index is 0 1 2 3 [4] where starting is 4
    
    # Here, -1 = stop index in a list
    # Explanation :
    # stop[index] = -1 (non-inclusive)
    # stop[index] = 0 (inclusive)
    
    # "hello" stop and include its [0] index which is h
    
    # Here, -1 = step size
    # Explanation :
    # start[index] + step size 
    
    # Since its negative it goes, start index at 4; then : 4 + (-1) = 3, 3 + (-1) = 2, 2 + (-1) = 1, 1 + (-1) = 0, 0 + (-1) = -1, (-1) stop index : end
    
    
    for char in range(len(string)-1, -1, -1)  :
        result = result + string[char]
    return result

print(ReverseString("hello"))
print(ReverseString("python"))