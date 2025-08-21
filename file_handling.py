'''
File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.

Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
'''

# writing or creating  a new file
with open("original_file.py", "w") as file:
    file_data = file.write("This is my original file")
    print(file_data)

# reading the original file
try:
    with open("original_file.py", "r") as file:
        original_content = file.read()
        print("Original Content:", original_content)

except FileNotFoundError:
    print("Error: The file does not exist.")

# modifying the content and writing to a new file

modified_content = original_content.replace("original", "modified")

with open("modified_file.py", "w") as new_file:
    new_file.write(modified_content)
    print("Modified content written to 'modified_file.py'.")   

'''
Hnadling Errors is best to handle inevitable errors that might occur while running codes
'''
file_name = input("Enter file name: ")     

try:
    with open(file_name, "r") as file:
        content = file.read()
        print("File Content:", content)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except IOError:
    print(f"Error: The file '{file_name}' cannot be read.")


