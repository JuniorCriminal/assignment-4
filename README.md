#🐍 Python Assignment4 – File Handling

This assignment demonstrates essential file handling operations in Python including reading, writing, appending, and exception handling.

📌 Task List

Read a File Using a Function with Exception Handling

Write, Append, and Read from a File

📖 Task 1 - Read a File Using a Function with Exception Handling

This script reads a file line-by-line using a custom function and includes exception handling for common issues like missing files or unexpected errors.

✅ Features

Takes a filename as input in the function call.

Opens and reads the file using a loop.

Strips extra whitespace or newlines from each line.

Handles the following exceptions:

File not found

Other unexpected exceptions

📁 File

task1.py

▶️ Sample Run

If sample.txt exists:

Hello world
This is sample text.


If file does not exist:

Error: The file 'sample.txt' does not exist.

✍️ Task 2 - Write, Append, and Read from a File

This script demonstrates how to:

Write user input to a file

Append additional input

Read and display the full content of the file

✅ Features

Takes user input and writes to a file.

Appends additional input to the same file.

Reads and displays the final content.

Uses file modes: w (write), a (append), and r (read).

Adds newlines automatically after each input.

📁 File

task2.py

▶️ Sample Run
Enter text to write to the file: Hello
Data successfully written to the output.txt

Enter additional data to append: World
Data successfully appended.

Final content of output.txt:
Hello
World

🧠 Concepts Used

File operations using open() with r, w, a modes

Exception handling with try-except

Looping through file lines

input() for dynamic user input

print() for formatted output

Feel free to use this as your base for creating or documenting your assignment. Let me know if you want help with the actual code too!
