total = 0
for i in range(1,6):
    while True:
        try: #try block to test a block of code for errors
            inpt = int(input("Enter int #{}: ".format(i)))
            total += inpt
            break
        except ValueError: #except block lets you handle the error if applicable.
            print("Invalid input. Please enter an int.")
            continue
        
print("Your sum is",total)