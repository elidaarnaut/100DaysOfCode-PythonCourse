# Instructions
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. (Including 100)

#Write your code below this row 👇
summ=0
for i in range(1,101):
    if(i%2==0):
        summ=summ+i
print(summ)