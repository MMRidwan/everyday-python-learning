import random
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
        
# print_integer(5)
        

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
       
# print_sum(1000)

# Number guessing game
# Write a guessing game. The program picks a secret number between 1 and 10. The user gets unlimited guesses. 
# Each wrong guess tells them if the secret number is higher or lower. When they guess correctly, print how many attempts it took and exit.

# Ex. Guess a number between 1 and 10: 5 Too low. Try again: 8 Too high. Try again: 6 Too low. Try again: 7 Correct! You got it in 4 attempts.
def number_guessing_game():
    hasGuessed = False
    counter = 0
    
    randomNumber = random.randrange(1, 11, 1)
    
    while(hasGuessed is not True) :
        guessedNumber = int(input("Guess a number between 1 and 10: "))
        counter += 1 
        result = ""
        if(guessedNumber > randomNumber) :
            result = f"Try again: {guessedNumber} Too high"
        elif(guessedNumber < randomNumber) :
            result = f"Try again: {guessedNumber} Too low"
        else :
            result = f"{guessedNumber} Correct! You got it in {counter} attempts."
            hasGuessed = True
            break
    print(result)
    
# number_guessing_game()

# Problem 4
# easy
# Multiplication table for 7
# Print the multiplication table for 7, from 7×1 to 7×10. Each line should be formatted exactly as shown below.
# 7 x 1 = 7 7 x 2 = 14 7 x 3 = 21 ... 7 x 10 = 70
# def multiplication_table (number = int(input("Enter Number for table : "))) :
#     hasCompleted = False
#     counter = 1
    
#     while(hasCompleted is not True) :
#         print(f"{number} x {counter} = {number * counter}")
#         counter += 1
        
#         if(counter == 11) :
#             hasCompleted = True
        
# multiplication_table()

# Problem 5
# medium
# FizzBuzz
# Print numbers 1 to 100. Multiples of 3 print "Fizz". Multiples of 5 print "Buzz". Multiples of both print "FizzBuzz". Otherwise print the number. 
# You've seen this before — now write it from memory without looking anything up.
# 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
def fizz_buzz() :
    result =""
    for counter in range(1, 101, 1) :
        if counter % 3 != 0 and counter % 5 != 0 :
            result = f"{counter} not FizzBuzz"
        elif counter % 3 == 0 and counter % 5 == 0 :
            result = "FizzBuzz"
        elif counter % 3 == 0:
            result = "Fizz"
        elif counter % 5 == 0:
            result = "Buzz"
        print(result)

# fizz_buzz()

# Problem 6
# medium
# Count vowels in a string
# Write a function that takes a string and returns the number of vowels in it. Vowels are a, e, i, o, u — case insensitive. Ignore everything else.
# count_vowels("hello") → 2 count_vowels("Python") → 1 count_vowels("aeiou") → 5 count_vowels("HELLO WORLD") → 3 count_vowels("rhythm") → 0
def count_vowels (input) :
    vowels = ["a", "e", "i", "o", "u"]
    counter = 0
    for char in input.lower():
        if char in vowels :
            counter += 1
            
    print(counter)

count_vowels("Python")   