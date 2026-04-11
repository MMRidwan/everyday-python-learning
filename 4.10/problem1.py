# Problem 1
# medium
# FizzBuzz — the classic filter
# Print numbers from 1 to 100. 
# But: for multiples of 3 print "Fizz", for multiples of 5 print "Buzz", for multiples of both print "FizzBuzz". Otherwise print the number.

# Everyone knows this problem. Very few people write the optimal version on the first try under pressure. The order of your conditions matters.
# Expected output (first 15): 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz

for i in range(1, 100) :
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
    elif i % 3 == 0 :
        print("Fizz")
    elif i % 5 == 0 :
        print("Buzz")
    else :
        print(str(i))