#Functions

#what is a function?
#a function is a block of reusable code (inside your program or even other programs) that performs a specific task.
# Functions help you organize your code, avoid repetition, and make programs easier to read and maintain.

#2 Give an example on how function squrt is used as a function:
# sqrt stands for square root. It's a function from the math module that returns the square root of a number.
#import math
# Use sqrt to calculate the square root
#number = 16
#result = math.sqrt(number)
#print(f"The square root of {number} is {result}")

#3explain in terms of a black box how functions work and why they are dependent on variables
# Imagine a function is a black box:
# You put something in (input)
# The box does something (processing)
# You get something out (output)
#
# You don’t always need to know how the box works inside — you just need to know: What goes in and What comes out


#What is an function definition, with what and how does it work?
#A function definition is how you create a function in Python.It's like giving your computer instructions that it can reuse whenever you "call" that function.
#def function_name(parameters):     #parameters is what goes in function, variables(this is the function head)
    # code block                    # all lines under describes what it looks like inside the black box  (this is the body of the function)
    #return something               # return does two things: decides what result from variable is going to be returned and terminates function. The  expression after "return" is a truthvalue of the type Bool


# the result from a function can be of any sort not just numerical

#give an example of a function that just does something without printing any result
# import datetime

# def write_date():         //paramaters defined by user
#   dt = datetime.datetime.now()    /date and time now
#   d = dt.date()           /todays date
#   print (str(d))          /writes out as yyyy/mm/dd
#there is no return statement here beacuse the function terminates automatically when last command is run. The function returns a "none"as a value


#what is necissary to do to actually make a calculation with function
# define function, then Call the function. if put function in beginning it is already defined by interpretor if you want to use it later in program.

#what is call by value?
#Call by value is a way of passing arguments to a function where:A copy of the actual value is passed to the function.Changes made to the parameter inside the function do not affect the original variable outside.
#You're giving the function a photocopy of the data — not the original. So any edits the function makes won't change the original outside
#you can´t change value of paramaters inside a definitionfunction because they are just copies

#how to we store the reult of a function?
#you need to take care of the returned value the function gives you by storing in a variable for later use
#def add(a, b):
    #return a + b  # Function returns the sum

#result = add(3, 4)  # Store the returned value in variable 'result'
#print(result)       # Output: 7

#give an example of a function that completley misses parameters
# random module
# import ramdom
# x= random.random()        /empty pharanthesis, gives parameters between 0<=x>=1

#you can use a funtion of the type bool as result and use call in ex. an if statement (if "true", else (when false)...)
# if function_name(the value you want to test):
#       print...
# else:
#       print...

#how many returns can a function give?
#functions only return ONE result at a time

#How to return multiple results from function by using a tuple in the return statement ?
# def sum_prod(a ,b)
#   return(a+b, a*b)        /resturns a tuple of both sum and product of a and b

# How can you now call the function from this tuple to fetch only one of the answers (sum or prod)
# t = sum_prod (2.0, 2.5)
# print (f"sum:     {t[0]})
# print (f"prod:     {t[1]})        #use indexing from tuple

#What are local variables?
# variables defined inside a function, and can only be used within that function.
# They exist only during the function’s execution, and disappear once the function finishes running.
#def greet():
    #message = "Hello, world!"  # 'message' is a local variable
    #print(message)

#greet()
# Output: Hello, world!

#print(message)
# ❌ Error! 'message' is not defined outside the function

#What are global variables?
#defined outside of all functions and is accessible from anywhere in your code, including inside functions
#se mera under globala och lokala värden, modulen 

#How to expessionaly write that you mean a lokal or global variable?
# x = 5
#
# def modify_global():
#     global x     # ← This makes it clear you're using the global variable
#     x = 10


#### functions can have text, lists and tuples as parameters ###

#In Python, a list variable is a reference to the actual list object in memory. This is especially important when passing lists to functions, because modifying the list inside a function also modifies it outside (since both refer to the same object). When you pass a list to a function, you're passing a reference, not a copy
# def add_item_safely(my_list):
#     my_list.append(100)
#     print("Inside function:", my_list)
#
# numbers = [1, 2, 3]
# add_item_safely(numbers.copy())  # Pass a copy instead
#
# print("Outside function:", numbers)  # Still [1, 2, 3]

#if you make changes in a list via the parameters , this will actually change the original list itself. Give example of Changing a List Through Function Parameters
#def modify_list(lst):
    #lst.append("new item")  # Modifying the list inside the function
    #print("Inside function:", lst)

# Original list
#my_list = ["apple", "banana"]

# Call the function with the list
#modify_list(my_list)

# Check the original list after the function call
#print("Outside function:", my_list)

#output
#Inside function: ['apple', 'banana', 'new item']
#Outside function: ['apple', 'banana', 'new item']

#text as parameters: write a function "alfa" that when called compares two text to one another:
#def alfa(s):
#   s=s.lower()
#   v=list(s)       #Converts the string into a list of characters.
#   for i in range (0,len(v)):
#       if v[i]== "ä":
#           v[i]= "å"
#       elif v[i]=="å":
#           v[i]="ä"
#   return v

#more about parameters:  Create a function using def and return that calculates compound interest.
#Include:
#The amount of money deposited in the bank,
#The interest rate per year, and
#The number of years the money stays in the account.

#def compound_interest(rate,capital, years):        #function has three parameters
    #return capital*(1+0.01*rate)**years

# now call the parameters with names:
# s= compound_interest(capital =100, rate = 1.2, year=10)
#tip! you can also combine the both BUT parameters with order first then parameters with names
# s= compound_interest(1.2, year =10, capital =100)

# What does / inside parameters mean?
# Parameters before / must be passed positionally (you cannot use their names when calling the function).
# Parameters after / can be passed either positionally or by keyword (named arguments).
#def func(a, b, /, c, d):
    #print(a, b, c, d)

# What are default arguments?
# It refers to values that a function uses automatically if no other value is provided when calling the function.
# def greet(name="Guest"):      #"Guest" is the default value for the parameter name
#     print(f"Hello, {name}!")      #If you call greet() without an argument, it will use "Guest".

# What does * operator do in "print(*...)" ?
#The * operator in print(*args) is called the unpacking operator (or splat operator). It unpacks an iterable (like a list or tuple) into separate arguments.
# normally print() can take multiple arguments:
# print(1, 2, 3)                #Output: 1 2 3

#numbers = [1, 2, 3]
#print(numbers)                 #Output: [1, 2, 3]  (prints the list as a single object)
# print(*numbers)               #Output: 1 2 3

#This tells Python to send each element of the list as a separate argument to print.

# How is type notations used inside function?
#def function_name(parameter1: Type1, parameter2: Type2) -> ReturnType:
    # function body

# def average(a:float, b:float) -> float:
#   return (a+b)/2

#you can have -> bool, -> None
#or if it is list: def raf_demo (a:list[float],x) -> float      #type: list[float]


#referenses to functions.
# def quad(x):
#   return x*x
# def cube(x):
#   return x *x *x
# Now assign: f = quad         #OBS! no parenthesis here! we created a variable with mane f

# the variable f will reference to the same function as the variable quad.

#test: a = f(3)         //gives 9
#test: a = quad(3)      // gives 9

#what is and how to use function "map"?
#The built-in Python function map() is very useful when you want to apply a function to every item in an iterable (like a list or tuple) — all in one line.

#map(function, iterable)
#function: A function that will be applied to each item.
#iterable: A list, tuple, or other iterable (like a string or range)

#what is and how to use function "filter"?
# The built-in filter() function is used to filter items from an iterable (like a list) based on a condition. It returns only the items for which the condition (a function) is True.

#filter(function, iterable)
#function: A function that returns True or False for each item
#iterable: The list, tuple, or other sequence to filter

#what is and how to use function "lambda"?
# A lambda function is a small, anonymous function in Python.
# It’s used when you need a quick function for a short task, often in one line — without formally defining it with def.

#lambda parameters: expression
#It can have any number of parameters
#But it must contain only one expression (no return, no multiple lines)
#example:
#double = lambda x: x * 2
#print(double(5))  # Output: 10

#what are two other functions that can have a reference for a function as a parameter?
# sorted and sort

# What are and how to use functions sorted and sort?
#Both are used to sort data, but they are used in different ways.
#sorted:
#Works on any iterable (like list, tuple, string), Returns a new sorted list, Does not change the original data

#sort:
#Can only be used on lists, Sorts the list in-place (modifies the original list), Returns None


#"Construct a function that calculates a root (zero) of mathematical functions. The function should have four parameters." give an example of how the first line would look?
# def root_nero(f,a,b,epsilon=le10):
# f = A function — this is the mathematical function for which you want to find a root (zero), such that f(x) = 0.
# a = A starting value (or interval start) — often used as the left bound or an initial guess.
# b = A second value (or interval end) — often the right bound of an interval or a second guess.
# epsilon = The tolerance — how close to zero the result should be for it to count as a root. 1e-10 means 0.0000000001. This sets the precision.


#What is a recursive function?
#A recursive function is a function that calls itself to solve a problem by breaking it into smaller parts.
# example the recursive function n!:
# def factorial(n):
#     if  n<0:
#         return None
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

#se mer under skapa egna funktioner och moduler 



