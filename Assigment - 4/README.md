# Task - 7.py

1. try Block open("sample.txt", 'r') attempts to open the file in read mode.

2. If the file exists: It reads and prints each line using a for loop.

3. Each print(content) shows one line at a time.

4.except FileNotFoundError as e : If the file sample.txt does not exist, this block handles the error.

5. e.filename gives the name of the missing file.

6. Prints finally Block:
This block always executes, no matter what happens above.




----------------------------------------------------------------------------------


# Task - 8.py

1.  Write to File :
Opens output.txt in write mode (w).
Takes user input and writes it to the file.
If the file already exists, it overwrites the previous content.


2. Append to File :
Opens output.txt in append mode (a).
Takes additional user input and appends it to the file.
\n ensures that appended text starts on a new line.


3. Read and Display File :
Opens output.txt in read mode (r).
Loops through each line and prints it.
If lines already have \n, this may cause extra blank lines in output.
