# Instructions
#Write a program that works out whether if a given year is a leap year.

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year%4 ==0:
    if year%100 == 0 and year%400 == 0:
        print("Leap year.")
    elif year%100 == 0 and year%400 != 0:
        print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")