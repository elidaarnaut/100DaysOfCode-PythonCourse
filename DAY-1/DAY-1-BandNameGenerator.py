#INSTRUCTIONS
#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line:
# Solution: https://replit.com/@appbrewery/band-name-generator-end

print("Welcome to the Band Name Generator! This is the end result of our day 1 of a 100 days of code challenge.\n")
city = input("What is the name of the city you grew up in? \n")
pet_name = input("What is the name of your pet? \n")
band_name = city + " " + pet_name
print("Your band name could be " + band_name)