#TO HANDLE TEXT
#1 What is literals?
# A literal is a fixed value that you write directly in your code. It represents itself (not a variable or expression). ex. numerical literals , string literals, boolean literals. Ex. x=42, 42 is a integer literal. or name = "Eva", Eva is a string literal. COMPARE TO y= x, Here y is not a literal, it’s a variable that refers to the value stored in x.

#2 What does "\" inside a string tell the program?
# That the next character is treated differently ex. x = "His name was \"Mikael\"". character combinations with "\" is called escape-sequenses.

#3 What is a "raw string", and how are they linked to backslashes - "\"
#Normally, in Python, backslashes (\) are used for escape sequences inside strings. A raw string tells Python “don’t treat backslashes as special — just keep them as they are.”
# path = r"C:\new_folder\test.txt"          here \n and \t escapes are ignored
# print(path)                               C:\new_folder\test.txt

#what is Unicode?
# Unicode is a system for representing characters (text) as numbers. It’s like a giant dictionary where every character in every language (letters, numbers, emojis, symbols) has its own unique number called a code point. So computers don’t actually store "😊" — they store 128522 ,  and Unicode tells them how to show it. There is unicode for digits, "0" → U+0030, So "0" as a string is different from the number 0 as an integer. Unicode is used instead of ASCII as a international standard.

#why is Unicode  used instead of ASCII
# ASCII Uses 7 bits → only 128 characters. Unicode Can represent over 1.1 million characters with UTF-8 (one byte), UTF-16 (two bytes) and UTF-32 (four bytes) groups.

#How can you print a character that is not on your keyboard using Unicode?
# use \u inside the string followed by the unicode, then print it
# print("\u03A9")   # Greek capital letter Omega (Ω)

#How can you print a character that is not on your keyboard using the charachters name instead of the unicode?
# use \N            OBS! knowing the official Unicode names is key if you want to use the \N{...} syntax in Python
# print("\N{GREEK CAPITAL LETTER OMEGA}")    # Ω
# to know name import Pythons´s "unicodedata" module
#import unicodedata
#char = "Ω"
#print(unicodedata.name(char))