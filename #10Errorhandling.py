#1 What are the 3 main different types of Errors in a program?
# SyntaxError: Problem in the code structure (violates language rules). Program won’t run at all. In C or Java called CompilationError.
# RuntimeError: Error that happens while the program is running. Program crashes during execution
# LogicalEroor: Code runs but gives wrong results. Caused by flawed logic

#2 What is "exceptions" during a runtimeError?
# Felsignal på svenska. Exceptions are errors that happen while a program is running, and they interrupt normal flow unless handled.
# An exception is raised when something goes wrong (e.g., file not found, division by zero). If not handled, the program crashes. You can use try and except to catch and handle exceptions.
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

#3 What is a traceback/stacktrace?
# A traceback is an error report Python shows when an exception occurs during runtime.
# It tells you: What kind of error happened (e.g., ZeroDivisionError), Where it happened (file name, line number), The call stack — the path the program took to get to the error

#4 How can we generate exceptions during RuntimeErrors using assert-statemnet or raise-statement?
# The assert statement is used to check if a condition is True during runtime, and if it’s False, it raises an AssertionError.
# Purpose: Used for debugging and validating assumptions in code. Automatically raises an error if a condition fails
# assert *expression, (parameters)

#5 The raise statement lets you manually trigger an exception whenever you want during runtime.
# Purpose: To force an error when a certain condition occurs. Useful for validating input or handling special cases.
# raise ExceptionType                 Raises the specified exception without any custom message or parameters.
# raise ExceptionType (parameters)    Raises the specified exception with parameters, usually a custom error message. The parameters provide details about the error.
# raise                               Re-raises the last active exception inside an except block, during try-except 

#6 What is operator "is" used for?
# The is operator checks if two variables refer to the exact same object in memory. Key points: is tests identity, not equality. Two variables can be equal (==) but not the same object (is).
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True (both refer to the same object)
print(a is c)  # False (different objects with same content)
print(a == c)  # True (contents are equal)

#7 How to handle exceptions (felsignaler)? Explain more!
# Using the try, except, else, and finally blocks. Contains of a try-part and multiple except-parts. If no error occurs the try part is excecuted, if errors occur the runtime terminates in try-part and the program directly jumps to except-part. Except-parts tells what kind of errors we can handle. Ex. valueError, divisionbyzeroError... 
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result is {result}")
finally:
    print("Execution finished.")

#8 How can we avoid  a program terminating, by catching all types of exceptions, no matter what type they have?
# You can catch all exceptions using a bare except or by catching the base exception class Exception and adding it at bottom. 
try:
    # Code that might raise any exception
    risky_code()
except Exception as e:
    print(f"Caught an error: {e}")
    print(type(e))
    # Program continues running here

# Important notes: Catching all exceptions can hide bugs and make debugging hard. It's best to catch specific exceptions when possible.

#9 Why do some functions return None in Python?
#Functions return None if they don’t explicitly return a value. None means “no value” or “nothing” in Python.

#10 Control of inputs: 

#11 You never return to the try-part if an error occurs there, then how to repeat code?
# By putting the try-part in a repetition-statement, while True. 

while True:
    try:
        num = int(input("Enter a number: "))
        break  # Exit loop if input is valid
    except ValueError:
        print("That's not a valid number, try again.")
        
print(f"You entered: {num}")


#OR USING RETURN WHEN USING FUNCTIONS exits entire function immediately and returns a value

def get_number():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num  # Exit the function and return the number
        except ValueError:
            print("That's not a valid number, try again.")

result = get_number()
print(f"You entered: {result}")



