# 6. LISTS: LISTS AND TUPLES

#1 We have looked intp sequences made out of strings ,what other types of sequences are there
#Lists and tuples are other types of sequences

#2 What is so special with lists?
# The elements in lists are ordered. We can number the elements in a list.

#3 What is a queue in a list?
# A queue is a data structure that follows The first element added is the first one to be removed. (FIFO = first in, first out)

#4 What is a deque in a list?
#double-ended queue. Unlike a normal queue (FIFO, where you add at the back and remove from the front), a deque lets you:
#Add (.append) elements at both ends
#Remove (.pop) elements from both ends
# used by import: "from collections import deque"

#5 What is a stack in a list?
# a stack is a data structure that follows The last element added is the first one removed. (LIFO =last in, last out)
# you do not need to import collections just to use append() and pop() when treating a list as a queue or stack.

#6 how many types of lists are there in python?
# ordinary Lists "[]" and Tuples "()" or no parenthesis
# unlike ordinary lists, you can change value of an element in a tuple list.

#7 what is a list with only one element called? how does that look like for a list resp. tuple? Create also an empty list and tuple
# singleton.
# list = ["lonely"]
# tuple = ("lonely",)       /if tuple consiste of one element always add comma at end

# list_0 =[]
# tuple_0 =()

#8 can you use indexing on a list or a tuple?
#yes , use list/tuple name and [index]

#when comparing two lists, they should be of the same type. list = list, tuple = tuple

#9 How is operator (for -) "in" used with list
# to run through the elements of a list

#10 how can you change item in a ordinary list? Example change a item in a list called "x"
# use "range" to change value in a ordinary list
# for i in range (0, len(x)):
# x[i]= 0
# Now list x = [0,0,0,0....]

#11 How can you exampine if a item is in a list called x?
# use operator "in"
# "zineb" in x          //gives true or false answer

#12 what is list comprehension, how is it used?
# List comprehension is used to create a new list by looping over something (like another list, a range, or any iterable). Instead of writing a full for loop, you can do it in one line.
# new_list = [expression for item in iterable if condition]

#new_list = name the new list
#expression → what you want to put in the new list (ex. i*i)
#item → each element in the iterable (i)
#iterable → something you loop through (like a list or range) in this case new_list
#if condition (optional) → filter elements

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

#20 add a new item to list v
# v.append (4)          /gives us [1,2,3,4]

#21 how to use operation "insert"
# v.insert (4, 5)           /gives us [1,2,3,4,5]
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

#24 How does a loop that terminates with break look like?
# while True:
#   s= input ...
#   if s ==":
#       break

#25 how to copy items on list from variable to another variable?
#v= [1,2,3,4,5]
#w = [0,0,0]
#w=v.copy()              #new value for list w = [1,2,3,4,5]
#but when changing anything i w, also changes in v. Beacause variables v and w share the same index and list. called a reference

#26 How to not get w and v to share the SAME list but still opy and be able to make changes without the other one changing
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






