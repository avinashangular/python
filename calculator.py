# Function to add two numbers

def add(num1, num2):
    return num1 + num2


# Function to substract two numbers

def substract(num1, num2):
    return num1 - num2;

# Function to multiply two numbers

def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers

def divide(num1, num2):
    return num1 / num2


print("Please select opeation - \n" \
    "1. Add\n" \
    "2. Substract\n" \
    "3. Multiply\n" \
    "4. Divide\n")

#Take input from the user
select = int(input("Select operations from 1, 2, 3, 4 :"))

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if select == 1:
    print(num1,  " + ", num2, " = ", add(num1, num2))
elif select == 2:
    print(num1, " - ", num2, " = ", substract(num1, num2))
elif select == 3:
    print(num1, " * ", num2, " = ", multiply(num1, num2))
elif select == 4:
    print(num1, " / ", num2, " = ", divide(num1, num2))
else:
    print("Invalid input")
