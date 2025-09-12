#Functions

#what is a function?
#a function is a block of reusable code (inside your program or even other programs) that performs a specific task.
# Functions help you organize your code, avoid repetition (apart from using loops), and make programs easier to read and maintain.

#2 Give an example on how function sqrt is used as a function:
# sqrt stands for square root. It's a function from the math module that returns the square root of a number.
#import math
# Use sqrt to calculate the square root
#number = 16
#result = math.sqrt(number)        #module.function(variable name)
#print(f"The square root of {number} is {result}")

#3explain in terms of a black box how functions work and why they are dependent on variables
# Imagine a function is a black box:
# You put something in (input)
# The box does something (processing)
# You get something out (output)
#
# You don’t always need to know how the box works inside — you just need to know: What goes in and What comes out


#4 What is an function definition, with what and how does it work?
#A function definition is how you create a function in Python. Think of when you call the function name using "()" as a pair of telephones talking to each other, you call a function to invoke it: "Hey ...-function, excute your code"
#def function_name(parameters):     #parameters is what goes in function, variables(this is the function head)
    # code block                    # all lines under describes what it looks like inside the black box  (this is the body of the function)
    #return something               # return does two things: decides what result from variable is going to be returned and terminates function. The  expression after "return" is a truthvalue of the type Bool


# the result from a function can be of any sort not just numerical

##################################5. give an example of a function that just does something without printing any result
# import datetime

# def write_date():         //paramaters defined by user
#   dt = datetime.datetime.now()    /date and time now
#   d = dt.date()           /todays date
#   print (str(d))          /writes out as yyyy/mm/dd
#there is no return statement here beacuse the function terminates automatically when last command is run. The function returns a "none"as a value


# 6 what is necissary to do to actually use a function
# define function, then Call the function. if put function in beginning it is already defined by interpretor if you want to use it later in program.

# 7 what is "call by value"?
#Call by value/call-by-reference is a way of passing arguments to a function where in pther programming languages:
# A copy of the actual value is passed to the function.
# Changes made to the parameter inside the function do not affect the original variable outside.
#You're giving the function a photocopy of the data — not the original. So any edits the function makes won't change the original outside
#you can´t change value of paramaters inside a definitionfunction because they are just copies

#In python no such thing! In python we have call-by-object reference, wether we can change the values depends wether the object is mutable or immutable (immutable ex. atrings, floats, integers)

# 8 how to we store the reult of a function?
#you need to take care of the returned value the function gives you by storing in a variable for later use
#def add(a, b):
    #return a + b  # Function returns the sum

# 9 result = add(3, 4)  # call function name, Store the returned value in variable 'result'
#print(result)       # Output: 7

# 10 give an example of a function that completley misses parameters
# random module
# import ramdom
# x= random.random()        /empty pharanthesis, gives parameters between 0<=x>=1

#11 How can you use a function of the type bool?
# A function of type bool is just a function that gives you either:
#True ✅ (yes, correct, go ahead)
#False ❌ (nope, don’t do it)
# if function_name(the value you want to test):

#def is_even(number):        #function to test if a num is even
    #return number % 2 == 0

#if is_even(4):
    #print("That's even!")
#else:
    #print("That's odd!")


#12 how many returns can a function give?
#functions only "return" once — but it can return multiple values at once.
# def say_hi():
    #return "Hi"     #to return multiple values, write them on same line
    #return "Hello"  # ❌ This line will never run


#13 Why is it samrt to use a tuple in the return statement? 
# to fetch only one of the values by using indexing
# def sum_prod(a ,b)
#   return(a+b, a*b)        /resturns a tuple of both sum and product of a and b

# t = sum_prod (2.0, 2.5)
# print (f"sum:     {t[0]})
# print (f"prod:     {t[1]})        

#14 What are local variables?
# variable names defined INSIDE a function, and can only be used within that function. They can´t be printed!
# They exist only during the function’s execution, and disappear once the function finishes running.
#def greet():
    #message = "Hello, world!"  # 'message' is a local variable
    #print(message)

#greet()
# Output: Hello, world!

#print(message)
# ❌ Error! 'message' is not defined outside the function

#15 What are global variables?
#defined outside of all functions and is accessible from anywhere in your code, including inside functions
#se mera under globala och lokala värden, modulen 
























#16 How to explicitly write that you mean a lokal or global variable?

# def my_function():
    #x = 5  # This is a local variable
    #print(x)

#x = 10  # This is a global variable
#def my_function():
    #global x       # ← This tells Python you're referring to the global 'x'
    #x = x + 5      # Modify global x
    #print(x)



#### functions can have text, lists and tuples as parameters ###

#17 In Python, a list variable is a reference to the actual list object in memory. This is especially important when passing lists to functions, because modifying the list inside a function also modifies it outside (since both refer to the same object). When you pass a list to a function, you're passing a reference, not a copy
#def add_item(my_list):
    #my_list.append("🍎")  # Add an item to the list
    #print("Inside function:", my_list)

#fruits = ["🍌", "🍊"]
#add_item(fruits)
#print("Outside function:", fruits)

#Inside function: ['🍌', '🍊', '🍎']
#Outside function: ['🍌', '🍊', '🍎']




#18 Give example of Changing a List Through Function Parameters. Because if you make changes in a list via the parameters , this will actually change the original list itself. 
#def change_list(my_list):
    #my_list[0] = 100  # Change the first item

#numbers = [1, 2, 3]
#change_list(numbers)
#print(numbers)

# Gives [100, 2, 3]


#19 text as parameters: write a function "alfa" that when called swaps any "ä" to "å" and any "å" to "ä".
#def alfa(s):
    #s = s.lower()      # Step 1: Convert all text to lowercase
    #v = list(s)        # Step 2: Turn the string into a list of characters
    #for i in range(len(v)):  # Step 3: Loop through each character
        #if v[i] == "ä":
            #v[i] = "å"        # Step 4a: Swap ä → å
        #elif v[i] == "å":
            #v[i] = "ä"        # Step 4b: Swap å → ä
    #return v           # Step 5: Return the changed list of characters


#20 more about parameters:  Create a function using def and return that calculates compound interest. Include:
#The amount of money deposited in the bank,
#The interest rate per year, and
#The number of years the money stays in the account.

#def compound_interest(rate,capital, years):        #function has three parameters
    #return capital*(1+0.01*rate)**years

# now call the parameters with names:
# s= compound_interest(capital =100, rate = 1.2, year=10)
# Tip! you can also “combine positional and named parameters”
# compound_interest(1.2, years=10, capital=100)


# 21 What does "/" inside parameters mean?
# Parameters before / must be passed positionally (you cannot use their names when calling the function) eg compound_interest(1.2, 100, 10)
# Parameters after / can be passed either positionally or by keyword (named arguments). eg. compound_interest(years=10, capital=100, rate=1.2) or compound_interest(1.2, 100, 10), or mix if positional

#def func(a, b, /, c, d):
    #print(a, b, c, d)

#22 What are default arguments?
# It refers to values that a function uses automatically if no other value is provided when calling the function.
# def greet(name="Guest"):      #"Guest" is the default value for the parameter name
#     print(f"Hello, {name}!")      #If you call greet() without an argument, it will use "Guest".
# greet()

#23 What does "*" operator do in "print(*...)" ?
# Called the unpacking operator (or splat operator). It unpacks an iterable (like a list or tuple) into separate arguments.
# normally print() can take multiple arguments:
# print(1, 2, 3)                #Output: 1 2 3

#numbers = [1, 2, 3]
#print(numbers)                 #Output: [1, 2, 3]  (prints the list as a single object)
# print(*numbers)               #Output: 1 2 3  (unpacks each item and prints them individually, separated by spaces)

#24 How is type notations used inside function?
#def function_name(parameter1: Type1, parameter2: Type2) -> ReturnType:
    # function body
    # return something

# def average(a:float, b:float) -> float:
#   return (a+b)/2        #function will return a float number

#you can have -> bool, -> None, -> Integer
#or if it is list: def name (a:list[float],x) -> float    


# 25 Creating referenses to functions, how?
# def quad(x):
#   return x*x

# def cube(x):
#   return x *x *x

# Now assign the function itself to a new variable f:
f = quad                       #OBS! no parenthesis here! we created a variable with mane f. The variable f will reference to the same function as the variable quad.
                               # “Hey f, you now point to the same function as quad.”

#test: a = f(3)         //gives 9
#test: a = quad(3)      // gives 9

#26 what is and how to use function "map"?
#The built-in Python function map() is very useful when you want to apply a function to every item in an iterable (like a list or tuple) — all in one line.

# map(function, iterable)
#function: A function that will be applied to each item.
#iterable: A list, tuple, or other iterable (like a string or range)

# 27 what is and how to use function "filter"?
# The built-in filter() function is used to filter items from an iterable (like a list) based on a condition. It returns only the items for which the condition (a function) is True.

#filter(function, iterable)
#function: A function that returns True or False for each item
#iterable: The list, tuple, or other sequence to filter

#28 what is and how to use function "lambda"?
# A lambda function is a small, anonymous function in Python.
# It’s used when you need a quick function for a short task, often in one line — without formally defining it with def.

# lambda "parameters":"expression"
#It can have any number of parameters
#But it must contain only one expression (no return, no multiple lines)
#example:
#double = lambda x :x*2
#print(double(5))  # parameter x=5 gives Output: 10

#29 What are two other functions that can have a reference for a function as a parameter?
# sorted and sort, apart from map(), filter()

# What are and how to use functions sorted and sort?
#Both are used to sort data, but they are used in different ways.

#sorted:
#Works on any iterable (like list, tuple, string), Returns a new sorted list, Does not change the original data. NOW ITS SORTED

#sort:
#Can only be used on lists, Sorts the list in-place (modifies the original list), Returns None. GIVES COMMAND TO SORT NOW...


#30 "Construct a function that calculates a root (zero) of mathematical functions. 
# The function should have four parameters." give an example of how the first line would look?
# def root_zero(f,a,b,epsilon= 1e -10):
# f = A function — this is the mathematical function for which you want to find a root (zero), such that f(x) = 0.
# a = A starting value (or interval start) — often used as the left bound or an initial guess.
# b = A second value (or interval end) — often the right bound of an interval or a second guess.
# epsilon = The tolerance — how close to zero the result should be for it to count as a root. 1 e-10 means 0.0000000001. This sets the precision.


#31 What is a recursive function?
# A recursive function is a function that calls itself to solve a problem by breaking it into smaller parts of the same problem, until it reaches a point where it stops (called the base case).
# example the recursive function n!:
# def factorial(n):
#     if  n<0:
#         return None
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# Imagine looking into two mirrors facing each other. 
# You see a reflection of yourself, reflected again and again, getting smaller each time — that’s kind of like recursion!


#se mer under skapa egna funktioner och moduler 



