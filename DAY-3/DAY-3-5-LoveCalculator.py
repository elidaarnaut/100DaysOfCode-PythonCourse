# Instructions
#You are going to write a program that tests the compatibility between two people.
#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs.
#Then check for the number of times the letters in the word LOVE occurs.
#Then combine these numbers to make a 2 digit number.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = name1.lower() + name2.lower()
count1= names.count('t') + names.count('r') + names.count('u') + names.count('e')
count2= names.count('l') + names.count('o') + names.count('v') + names.count('e')


scoreStr = str(count1) + str(count2) 
score = int(scoreStr)
if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
