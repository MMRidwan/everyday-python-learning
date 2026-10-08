while True:
    value = input("Enter a positive number: ")
    if value.isdigit() and int(value) > 0:      #This is taking in a string
        break
    elif value == "0":
        print("TF")
    else:
        print("Try again.")