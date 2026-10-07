# Handling invalid user input
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Error: Please enter a valid number.")

# Handling division by zero
try:
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide a number by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")

# Handling file not found
try:
    with open("data.txt", "r") as file:
        data = file.read()
        print("\nFile content: ")
        print(data)
        file.close()
         
except FileNotFoundError:
    print("Error: The file was not found.")