# Instructions
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
#You have x days, y weeks, and z months left.
#Where x, y and z are replaced with the actual calculated numbers.
#Example Input -> 56
#Example Output -> You have 12410 days, 1768 weeks, and 408 months left.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

myAge = int(age)

dieMonth = 90*12
dieWeek = 90*52
dieDays = 90*365

daysLeft = dieDays - (myAge*365)
weeksLeft = dieWeek - (myAge*52)
monthsLeft = dieMonth - (myAge*12)

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")