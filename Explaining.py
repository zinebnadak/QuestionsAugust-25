dog_years  = int(input("Enter number of dogyears?:"))

if dog_years == 1:
    human_years = 15
elif dog_years == 2:
    human_years = 15 + 9
elif dog_years > 2:
    human_years = 15 + 9 + (dog_years-2)*5
else:
    human_years = 0     #for neg values or 0

print (f"human years:{human_years}")








