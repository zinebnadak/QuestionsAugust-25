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

#8 What are sequences in Python?
# In Python, sequences are ordered collections of items/elements that support indexing, slicing, and iteration.
# Common sequence types include lists, tuples, strings, and ranges.
# They allow you to access elements by position and perform operations like concatenation, repetition, and membership tests.

#9 How does indexing work?
# The items/elements in a sequence are numbered starting from 0 (or backwards from -1), and their number is called index.
#x = "Hello!"    /the letter "H" has index 1, "e" index 2 etc

#10 How can you read the corresponding item/element, by knowing the indexing number. Eg. indexing?
# write the variable then the indexnumber you want to know inside "[]"
# x[0]          /will give you H

#11 How to know how many items/elements are in a sequence? (by using only the variable)
# use function "len"
# print (len (x))   /will give you 6


#12 Unlike other languages ,In python you can use negative indexes to begin counting from backwards.

#13 In indexing you can choose only one item from sequene, How can you selcet multiple?
# By creating a "slice" that becomes the new sequence - ex. sequence [first:last:steps]
# leaving first gives you index 0
# leaving last gives you the sequances lenght /         /you can leave one or two integers empty, but ":" should always be included
# Leaving steps gets you automatically 1
# you an actually go beyond the limits of indexes when slicing , s[1:100] can give you whole sequence

#14 How and why can we compare sequences?
# to see if they are equal (same lenght and items gives you True)
# "abc" = "abc"         //give True

#15 How can you compare if a sequence is smaller or bigger than another?
# by using lexicographic order/dictionary order
# "abc" < "abcd"    // give True

#16 what is it that gets compare when comparing texts
# When comparing texts (strings) in Python, what gets compared is the Unicode code point (numeric value) of each character, in lexicographic order.
# "å" < "ä"         /gives false, bcs it goes by the numerical code , only letters a-z are in "right order" even numerical.



