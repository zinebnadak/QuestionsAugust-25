#1 How does the rounding when converting float number to integer work
#Answer: Floats are always rounded downwards :y= 2.7, print(int(y)) gives you 2

#2 Give me two ways to determine the amounts of deciamls in rouded value
#Answer:
# by using round and adding ,1 after variable: _pi = 3.14 - print(round(_pi, 1))
# using f string:_pi =3.14 - print (f"{x:.1f}")

#3 Write a program that calculates Volume V and Area A for a sphere of radius r. Print the values of the variables with a precision of 3 decimal places.
#Answer:
import math
# Be användaren om radien
r = float(input("Ange radien r: "))
# Beräkna volym och area
v = (4 * math.pi * (r ** 3)) / 3
a = 4 * math.pi * (r ** 2)
# Skriv ut resultat med 3 decimalers noggrannhet
print(f"Volymen är: {v:.3f}")
print(f"Arean är: {a:.3f}")

#7 How can you shorten this code to only two lines code?
#data = input("Enter a number: ")
#data = float(data)                 # Converts string "3.14" that input returns to number 3.14
#print("The number is ", data)

#Answer:
#data = float(input("Enter a number: "))
#print("The number is ", data)

^#8 How can you input multiple data, though input only reads in one string of data?
#Answer:
#value1 = input("Skriv in tre värden: ")
#value2 = input()
#value3 = input()
#print("Du skrev in:", value1, value2, value3)

#9 What is split used for, and how to use?
#Answer: splits one string of text into smaller parts. Used to input multiple values on the same string. Used with pointsyntax.  Can combine split with input.
# text = "Hello world this is ChatGPT"
#words = text.split()
#print(words)
#Output:
#['Hello', 'world', 'this', 'is', 'ChatGPT']

^#10 How can you combine split with input?
#Answer:
# answer = input("Enter three values: ")
#value1, value2, value3 = answer.split() 
# print("You wrote:", value1, value2, value3)
#eller
# answer = input("Skriv in tre värden: ").split()
# print("You wrote:", value1, value2, value3)

#11 what does () in ".split()" tell us?
#Answer: the different values of inputs are separated by blank space

#12 How can you change that?
#Answer: by specifying the separator inside the parenthesis
#ex. answer.split(":")        # Specify : as separator with quote sign

#12 For what practical things use split syntax? give example
# For processing using data of ex. time or date.
# Ex. Date:
# answer = input("Enter a time (HH:MM:SS): ")
# hours, minutes, seconds = answer.split(":")  # Specify ':' as separator
# print("You entered:", hours, minutes, seconds)

# 13 Exercise: Write a program that lets the user enter their birthdate in the format DD/MM/YYYY. Use input and split. Store the answer in three separate variables. What happens if the user only enters two values, or uses the wrong separator?
#Answer:

#14 What is sep="  and how is it used inside string?
#Answer: defines the separator that is inserted between the items you're printing.
# print("2025", "08", "25", sep="-")

^#15 Exercise: birthday calculation program. Calculate how old the person has become this year/will be in 10 years
#Answer:
print()
birthdate = input("When were you born? (DD/MM/YYYY): ") #Ask the user for their birthdate in the format DD/MM/YYYY
day, month, year = birthdate.split("/")
todays_year = int(input("What year is it now?:")) #Ask what year it is now
age = todays_year - int(year)   #Calculate how old the person is
print (f"You turned {age} years old {int(day)}/{int(month)}/{todays_year}")#Calculate how old the person has become this year and Print the result using an f-string

#Calculate how old the person will become in specified future year
print()
birthdate = input("When were you born? (DD/MM/YYYY): ") #Ask the user for their birthdate in the format DD/MM/YYYY
age_in_question = int(input("In what year do you want to know your age?:")) # Ask target year

day, month, year = birthdate.split("/") # Split the date into day, month, and year
birth_year = int(year) # Convert year to integer
age_in_that_year = age_in_question - birth_year
print (f"In {age_in_question}, you will be {age_in_that_year} years old!" )


#16 Explain what each symbol in the f-string mean?
#Answer: (f"text1{value:y.x}")
#f = formatted string
#{what:how}
# y.x where x is number of decimals and y is for padding

#17 How is tripple quotes """ used
#ANswer: to create a string that spans multiple lines




------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#18 Explain the von Neurmann arcitecture from 1945: EXAM QUESTION
#answer: 
#Lagrat program/lagring SSD/Hårddisk – Data och instruktioner lagras i samma minne.
#Enhetligt minne RAM – Samma minne används för både program och data.
#Processor  - CPU (Centralenhet) – Utför instruktionerna steg för steg. Består av tre delar: ALU (räkningar och logik), CU (Styrenhet-kontrollerar ordningen) och Register (små, snabba minnesplatser, används för att lagra data och instruktioner temporärt medan de bearbetas)
#
#In- och utmatning – Hanterar kommunikation med användare och enheter.ex. tangentbord, skärm 

#19 Explain how the different parts work together: EXAM QUESTION
#Samspel:
#1Du öppnar ett program från lagringen.
#2Det laddas in i minnet (RAM) - tömms när ström kopplas ur
#3Processorn kör instruktionerna.

#20 Identifiate the different parts from a picture from manual EXAM QUESTION
#Answer: search for pic

#21 Why is this important to understand? EXAM QUESTION
#Answer: The operating system’s job is to go from hardware to app. The operating system manages the hardware (processor, memory, hard disk, etc.) and enables programs and apps to use the hardware, creating an environment where programs can run.

#22 What is cache-memory used for?
#Answer: Cache memory is a small, super-fast type of memory inside the CPU used to store frequently accessed data and instructions. It helps the processor work faster by reducing the time needed to get data from the main memory (RAM).

#23 Storage media are devices where data is saved permanently or temporarily in a computer or other electronics.
#ANswer: Examples of storage media:
#Hard disk drive (HDD)
#SSD (Solid State Drive)
#USB flash drive
#CD/DVD
#Obs! with time the voltage redues and you an lose the stored media

#24 What is RAID? Raid 0 and Raid1? 
#Answer: RAID är ett sätt att koppla ihop flera hårddiskar eller SSD:er så att de fungerar tillsammans. Det kan göra datorn snabbare eller skydda dina filer bättre. Raid1 (spegling) =Samma data sparas på två diskar, som en kopia. Om en disk går sönder finns alltid en säker kopia kvar., Raid0 (striping) = Datan delas upp och sparas på flera diskar samtidigt. Gör datorn snabbare när den läser och skriver.Men om en disk går sönder, förlorar du ALL data. Olika RAID-typer gör olika saker med datan. Övriga nummber Raids är varianter av Raid 1 och 0. Avancerade system kan använda kombinationer av RAID, som RAID 10 (en blandning av RAID 1 + RAID 0).

#25 What is over-clocking?
#Answer: Overclocking means making a computer component run faster than its official speed set by the manufacturer — usually the CPU (processor) or GPU (graphics card) 

#26 What is motherboard?
#Answer: Moderkortet är den viktigaste kretskortet i en dator. Det är som datorns “hjärta” eller “nav” där alla viktiga delar kopplas ihop.
#På moderkortet sitter bland annat:
#Processor (CPU)
#Minne (RAM)
#Lagringsenheter (SSD/HDD)
#Grafikkort (ibland integrerat eller via plats)
#Flera anslutningar för USB, ljud, nätverk med mera

#27 What is SATA?
#Answer: SATA står för Serial ATA (Serial Advanced Technology Attachment). Det är en vanlig standard för att koppla hårddiskar och SSD-enheter till moderkortet i en dator. Används ofta för både HDD och vissa äldre SSD:er.
