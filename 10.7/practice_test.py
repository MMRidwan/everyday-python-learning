# Checkpoint: Classify a number as positive, negative, or zero using if/elif/else. 
# Then explain, out loud or in writing, why if []: doesn’t run.

def find_numbers(inputNumber) :
    try:
        value = int(inputNumber)
    except (ValueError, TypeError):
        return "Enter Valid Number!!"
    
    if(value > 0):
        print(f"{value} is Positive")
    elif(value == 0):
        print(f"{value} is Zero")
    else :
        print(f"{value} is Negative")
        

find_numbers(4)
find_numbers(-2)
find_numbers("3.5")
find_numbers(3.5)
find_numbers(0)


