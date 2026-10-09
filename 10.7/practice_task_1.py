# Problem 1 — FizzBuzz for One Number (difficulty: Easy · warm-up; not a direct LeetCode problem — 
# it’s the single-number decision core of LC #412 Fizz Buzz, which is solved with a loop over many numbers)

# Every loop-based FizzBuzz (you’ll meet the loop version Sunday, Oct 11) is this exact decision repeated once per number. 
# Get the single-number branching right tonight and Sunday is just “do this inside a loop.”

# Worked example (trace-first). n = 15.

n = 15
if(n % 3 == 0  and n % 5 == 0):
    print("Fizz Buzz")
elif(n % 3 == 0 ):
    print("Fizz")
elif(n % 5 == 0) :
    print("Buzz")
else :
    print("Nothing")
