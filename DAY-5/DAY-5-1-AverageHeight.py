# Instructions
# You are going to write a program that calculates the average student height from a List of heights.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
summ=0
counter = 0
for i in student_heights:
  summ= summ + i
  counter= counter + 1
average_h = round(summ/counter)
print(average_h)