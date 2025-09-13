#1 What is so special about the data you write in different variables in a program, when you terminate a program?
# When a program terminates, the data in its variables disappears — and that’s what makes it special and important. Variables hold the program’s "memory". Data must be saved before termination. Everything in RAM is cleared. If not saved = Lost forever
# The data in variables is special because it only lives during the program’s execution. If you don’t save it before the program terminates, it's lost permanently.
# --> files are saved in computers harddrive

#2 What is a textfile?
# A text file is a simple file that contains only readable characters (letters, numbers, symbols), usually stored with a .txt extension.

#3 How can you edit a textfile?
# Using a texteditor
# Notepad on Windows
# Textedit on Mac
# Using a code editor (more advanced): Open with editors like VS Code, Sublime Text, or Atom. These editors support syntax highlighting and search tools, but you can still edit .txt files easily


# The most simplest form of textfiles use an byte (8-bit) fo every charachter

#4 What does it mean that a file is stored according to UTF-8?
# UTF-8 means the file stores text in a universal format that supports almost all characters and languages — not just English letters. It supports all Unicode characters (letters, emojis, symbols, etc.)
# It's compatible with ASCII (so old systems still work)

#5 Python uses so-called streams to read and write data. Explain!
# In Python, when you read from or write to files, you're using a stream — a flow of data between your program and some input/output source (like a file, keyboard, or screen)
# A stream is like a pipeline that carries data:
Input stream: Data flows into your program (e.g., reading a file).
Output stream: Data flows out from your program (e.g., printing or writing to a file).

#6 What are file-objects?
# A file object is a special Python object that lets you interact with a file — such as reading, writing, or modifying it. 
# You create a file object using the built-in open() function. It provides methods like .open(), .read(), .write(), .close()
# ex. file.close()    where "file" is a file object

#7 There are three predefined streams
#Standard Input (stdin): Where the program gets input (usually from the keyboard).
#Standard Output (stdout): Where the program sends normal output (like what you see from print()).
#Standard Error (stderr): Where the program sends error messages separately from normal output.

#8 How do you use the open() function in Python to open a file by specifying its file path?
# To use the open() function with a path in Python, you just pass the file’s path as a string to open(). This path can be either:
# Relative path (relative to current working directory)
file = open("folder/data.txt", "r", encoding='utf-8')  # Opens 'data.txt' inside 'folder' relative to current directory

# Absolute path (full path from the root)
file = open("/Users/yourname/Documents/data.txt", "r")  # Full path on macOS/Linux

#9 What is the most bascic function call to open()? And how to use .close?
f = open(filename, mode , encoding="coding") 
f.close()                  # Close file
f.closed                   # bool to check if file closed

Using arguments:
filename — path or name of the file
mode — how to open the file ("r", "w", "a", etc.)
encoding — the text encoding to use (like "utf-8")

Important:Always close files after you're done to avoid data loss or file corruption. Alternatively, use with statement to auto-close files (recommended):

#10 How and when to use a "with" (as) -statement?
# Use a with statement every time you work with files in Python to handle opening and closing automatically and safely. 
# It’s best practice because it ensures files are properly closed without extra code.
# It opens the file and closes it automatically when done, even if errors occur.

with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello, world!\n")
    f.write("This is written using a with-statement.\n")
# File is automatically closed here

with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    sentences...
# Both files are automatically closed here

#11 Give example of more operators for text streams

f = open("file.txt", "r", encoding="utf-8")  # Open file with encoding
text = f.read()             # Read entire content
line = f.readline()         # Read one line
lines = f.readlines()       # Read all lines as list

print(f.name)               # Get file name
print(f.encoding)           # Get file encoding
text = f.read()             # Read entire content
line = f.readline()         # Read one line
lines = f.readlines()       # Read all lines as list
f.write("Hello\n")          # Write text
f.writelines(lines)         # Write multiple lines
for line in f:              # Iterate over lines
    print(line)
f.seek(0)                  # Move cursor to start
pos = f.tell()              # Get current position
print(f.closed)             # Check if file is closed
f.close()                  # Close file


#12 Two main ways to use python code to change in a file?
# Using a List      - Not efficient for very large files (uses a lot of memory).
Read the entire file into a list of lines.
Modify the list in memory.
Write the modified list back to the file.
    

# Using a Temporary File        - Efficient for large files (processes line-by-line). Safer because original file isn't overwritten until processing is complete.
Read the original file line-by-line.
Write modified lines to a temporary file.
Replace the original file with the temporary file.

#13 what function to create a new temporary file?
# tempfile.TemporaryFile('w+t')

#14 How to start python interpreter when running a python file in script-mode?
  # use commando py or python3 and filename.py in commandowindow
  ex. python3 filename.py

#15 How and why to use list "sys.argv" in main
  # sys.argv is a list that stores command-line arguments passed to a Python script. Use it in your main function to access inputs or options users provide when running the script. The first item, sys.argv[0], is the script name; the rest are the actual arguments.

  from sys import argv

def main(args):
    print("Arguments passed:", args)

if __name__ == "__main__":
    main(argv[1:])  # Pass arguments except script name


