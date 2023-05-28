#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip generator! This is the final project of day 2 of 100 days of code using Python!\n")
bil = input("What was the total bill? ")
p = input("What percentage tip would you like to give? 10, 12 or 15? ")
ppl = input("How many people to split the bill? ")

bill = float(bil)
percentage = int(p)
people = int(ppl)

ourPerc = (bill*percentage)/100
percPerPerson = round((ourPerc+bill)/people,2)
print(f"Each person should pay: ${percPerPerson}")