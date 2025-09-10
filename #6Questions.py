# 6. LISTS: LISTS AND TUPLES

#1 We have looked intp sequences made out of strings ,what other types of sequences are there
# Ranges, Lists and tuples are other types of sequences

#2 What is so special with lists?
# The elements in lists are ordered. We can number the elements in a list. And only type of sequence that is mutable (changeable)

#3 What is a queue?
# A queue is a data structure that follows The first element added is the first one to be removed. (FIFO = first in, first out). Lists are the only sequence-type supports this data structure.
# Key Characteristics of a Queue:

# Enqueue: Add an item to the end of the queue.
# Dequeue: Remove an item from the front of the queue.
# Peek: Look at the item at the front of the queue without removing it.
# Empty: Check if the queue is empty.

#4 What is a deque in a list?
# double-ended queue. The best option in Python for implementing a queue is deque (double-ended queue) from the collections module. Unlike a normal queue (FIFO, where you add at the back and remove from the front), a deque lets you:
# Add (.append) elements at both ends
# Remove (.pop) elements from both ends
# used by import: "from collections import deque"

#Here is an example that demonstrates a situation where using a deque is beneficial. Let's say you have a list of ingredients and you want to keep track of only the most recent three you've used.
from collections import deque

# We can initialize a deque with a max length
recent_ingredients = deque(maxlen=3)

print(f"Initial list: {recent_ingredients}")

# Add the first three items.
recent_ingredients.append("tomat")
recent_ingredients.append("gurka")
recent_ingredients.append("äpple")
print(f"After adding three items: {recent_ingredients}")

# Add a fourth item.
# This automatically removes the oldest item ("tomat")
recent_ingredients.append("fisk")
print(f"After adding a fourth item: {recent_ingredients}")

# Add a fifth item.
# "gurka" is automatically removed
recent_ingredients.append("bröd")
print(f"After adding a fifth item: {recent_ingredients}")

#what is difference between queue and dequeue?
#A deque (double-ended queue) is a versatile data structure that is designed for fast appends and pops from both ends. It is part of the collections module. The append() method adds an element to the right side (the end) of the deque.

#5 What is a stack in a list?
# a stack is a data structure that follows The last element added is the first one removed. (LIFO =last in, last out)
# you do not need to import collections just to use append() and pop() when treating a list as a queue or stack.

#  We'll simulate stacking and unstacking books.
# Create an empty list to act as our stack
books = []

print("Our stack is empty:", books)

# PUSH an item onto the stack using append()
# This adds the book to the top of the stack.
books.append("book 1")
books.append("book 2")
books.append("book 3")

print("Books pushed onto the stack:", books)

# POP an item from the stack using pop()
# This removes the last item that was added ("book 3").
last_book = books.pop()

print("Book removed (popped):", last_book)
print("Books left on the stack:", books)

# Pop the next item
next_last_book = books.pop()

print("Book removed (popped):", next_last_book)
print("Books left on the stack:", books)


#6 what is key difference between lists and tuples? 
#The key difference between them is mutability, both are sequences supporting indexing, slicing and iteration


#7 what is a list with only one element called? how does that look like for a list resp. tuple? Create also an empty list and tuple
# singleton.
# list = ["lonely"]
# tuple = ("lonely",)       /if tuple consiste of one element always add comma at end, to differentiate it from a simple parenthetical expression.

# list_0 =[]
# tuple_0 =()

#when comparing two lists, they should be of the same type. list = list, tuple = tuple

#9 How is operator "in" used with list
# The in operator in Python is used with a list to check if an element exists within it. 
# It's a boolean operator, which means it returns either True or False.
# for *item_name or *iteration in *list

#10 how can you change item in a ordinary list? Example change a item in a list called "x"
# use "range" to change value in a ordinary list
# for i in range (0, len(x)):
# x[i]= 0
# Now list x = [0,0,0,0....]

#11 How can you examine if a item is in a list called x?
# use operator "in"
# "zineb" in x          //gives true or false answer

#12 what is list comprehension, how is it used?
# List comprehension is used to create a new list by looping over something (like another list, a range, or any iterable). 
# It's a single line of code that combines the loop and the creation of new elements into one expression, making your code more readable and often faster

# new_list = ["expression" for "item" in "iterable" if "condition"]
#new_list = name the new list
#expression → what you want to put in the new list (ex. i*i)
#item → each element in the iterable (i)
#iterable → something you loop through (like a list or range) in this case new_list
#if condition (optional) → filter elements

#squares = []
for x in range(1, 6):
  squares.append(x**2)
print(squares) # Output: [1, 4, 9, 16, 25]

#squares = [x**2 for x in range(1, 6)]
print(squares) # Output: [1, 4, 9, 16, 25]


#13 How to use function "join" for lists?
# writes a single string  contained of all items in list
# print ("separator".join(lists_name))

#14 How to choose random element from list?
#import random
# item = random.choice(x)
# print(item)

#random module is very useful! :)

#THE ORDINARY LIST , type list

#15.How to make a list out of an input? (string)
# ex.
# input = input("write some words (use empty space as separator): ")
# list = input.split ()         / (",")or whatever separator is used by the inputter
# print (list[0])           //will fetch first word instead of whole string input




























#16 when can it be a good idea to combine ".replace" and ".split"
# when the input is for ex. : input = "a,b, c,  d"      /and we want to remove the viraety of empty spaces before splitting
# input = input.replace (" ", "  ")
# list = input.split (",")             /then create new list , list comprehension
# print (list)          / gives us ["a", "b", "c", "d"] without unregular empty spaces


#17 how to use list omprehension to turn strings in a list to be read as floats ?
# numbers = [float(i) for i in x]            /new list , from old list "x" called "numbers"


#18 a lists items can be changed, how? using indexing?
# list = [1, 2, 4]
# list [3] = 3          /feth the indexnumber of desired item , and set new value using =

#look at different functions used for list-type page 116.

#19 how is operation  "list" used?
# to form a list
# x = (1,2,3)
# v = list()        /empty list
# v = list(t)
# print (v)             /gives us [1,2,3]

#all operations is used by naming the index number! 

#20 add a ONE new item to list v
# v.append (4)          /gives us [1,2,3,4]

#21 how to use operation "insert"
# v.insert (5,6)           /gives us [1,2,3,4,5]
# first argument is index number, second argument new item

#22 how to use operation "del"
# del v [indexnumber]
# del v [indexnumber:indexnumber]

#23 when to use "pop" insted of "del"
# Removes an element and returns it. By default, removes the last item (pop()), but you can also give an index (pop(0)).
# Useful when you want to use the removed value.
# x = v.pop (4)
# print (x)             /gives 5
# print (v)             /gives the list without 5: [1,2,3,4]

#.clear() = removes all items
#. reverse() = rewrites list starting bakwards

#25 how to copy items on list from variable to another variable?
#v= [1,2,3,4,5]
#w = [0,0,0]
#w=v.copy()              #new value for list w = [1,2,3,4,5]
#now w and v are each others references 
#but when changing anything i w, also changes in v. Beacause variables v and w share the same index and list. called a reference

#26 How to not get w and v to share the SAME list but still copy and be able to make changes without the other one changing
# w = v.copy()

#27 lists in lists is called multidimentional lists, give an example of a two dimentional list
m = [[1,2],[3,4],[5,6]]       #list m has a list with three elements, each element is a list with two elements

#28 what is the mathematical word "matrix"
#A matrix is a rectangular array of numbers, symbols, or expressions, arranged in rows and columns
# list m has three rows and two columns

#29 to be able to continue writing list on next row in program use / or just any form of parenthesis works

#30 how to fetch sole elements on a two dimentional list?
# use indexing with integers as normal m[0][1]        // gives you element "2"

#31 How to print two dimentional lists neater and more readable?
#for i in range (0, len(m)):        /loops three times , one for every row (3 rows)
#    for j in range (0, len(m[i])):         /loops two times, one for every column (2 columns)
#        print (f"{m[i][j]:3}", end="")          //3 white spaes between each
#    print()                                /new row , before starting on new element-list in m
#loop through all elements and print them one by one

#32. On the same list use a different method, than for-range, printing two dimentional lists neater and more readable
#for i in m:
    #for r in i:
        #print(f"{r:3}", end="")
    #print()






