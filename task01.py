# Creating and writing data into a file
file = open("student.txt", "w")
file.write("My name is Shazmeen.\n")
file.write("I am learning Python in my InternNova internship.\n")
file.close()

print("File created and data written successfully.")

# Reading data from the file
file = open("student.txt", "r")
data = file.read()
file.close()

print("\nFile content: ")
print(data)

# Appending new data to the file
file = open("student.txt", "a")
file.write("This is week 04 of my Python programming internship.")
file.close()

print("New data added successfully.")

# Reading the updated file
file = open("student.txt", "r")
updated_data = file.read()
file.close()

print("\nUpdated file content: ")
print(updated_data)