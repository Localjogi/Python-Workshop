def userInput():
    first_input = int(input("Enter the first number: "))
    second_input = int(input("Enter the second number: "))
    return first_input, second_input

def add(a=0,b=0):
    return a+b

def sub(a=0,b=0):
    return a-b

def mult(a=0,b=0):
    return a*b

print("Welcome to Calculator")

while True:
    print("\nSelect an option:\n 1: Add \n 2: Subtract \n 3: Multiply \n 4: Stop")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a, b = userInput()
        print("Result:", add(a, b))
    elif choice == 2:
        a, b = userInput()
        print("Result:", sub(a, b))
    elif choice == 3:
        a, b = userInput()
        print("Result:", mult(a, b))
    elif choice == 4:
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
