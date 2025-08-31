# Step 1: Take user input and write it to a file
a1 = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(a1 + "\n")  #this function add input to the file from a1 that user give as input and \n add a newline.

print("Data successfully written tp the output.txt")

# Step 2: Take additional input and append it to the same file
a2= input("Enter additional data to append: ")

with open("output.txt", "a") as file:
    file.write(a2 + "\n")  #this function add input to the file from a2 that user give as input to add in output.txt and add a newline

print("data successfully appended.")

# Step 3: Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
