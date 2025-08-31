# Python Assignment 4
This assignment demonstrates essential file handling operations in Python including reading, writing, appending, and exception handling.

---

## 📌 Task List
___
1. [ Read a File Using a Function with Exception Handling](#-task-1---Read-a-file-Using-a-Function-with-Exception-Handling)
2. [Write,Append,and Read from a Files](#-task-2---Write,Append,and-Read-from-a-Files)

---

## 🧮 Task 1 -  Read a File Using a Function with Exception Handling
___
This script reads a file line-by-line using a custom function and includes exception handling for common issues like missing files or unexpected errors.

### ✅ Features
___
- Takes a filename as input in the function call.

- Opens and reads the file using a loop.

- Strips extra whitespace or newlines from each line.

- Handles the following exceptions:

  - File not found

  - Other unexpected exceptions

### 📁 File
___
`task1.py`

### ▶️ Sample Run
___
If `sample.txt` exists:
    it prints lines that exists in it
```commandline
Hello world
This is sample text.
```
If file does not exist:
```commandline
Error: The file 'sample.txt' does not exist.
```

## 📊 Task 2 -  Write,Append,and Read from a Files

___
This script demonstrates how to:

- Write user input to a file

- Append additional input

- Read and display the full content of the file
### ✅ Features
___
- Takes user input and writes to a file.

- Appends additional input to the same file.

- Reads and displays the final content.

- Uses file modes: `w` (write),` a` (append), and `r` (read).

- Adds newlines automatically after each input.

### 📁 File
___
`task2.py`

### ▶️ Sample Run
___
```commandline
Enter text to write to the file: Hello, python
Data successfully written to the output.txt

Enter additional data to append: Learning file handling in python.
Data successfully appended.

Final content of output.txt:
Hello,python
Learning file handling in python.
```

---

## 🧠 Concepts Used
___
File operations using `open()` with `r`, `w`, `a` modes.

Exception handling with `try-except`.

Looping through file lines.

- `input()` for dynamic user input.

- `print()` for formatted output.
---
