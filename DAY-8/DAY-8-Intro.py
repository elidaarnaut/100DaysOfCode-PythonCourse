# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("Hi!")
#     print("What's up")
#     print("Nice to meet you" )

# greet()

#function that allows for inputs
# def greet_with_name(name):
#     print(f"Hi {name}!")
#     print(f"What's up {name}")
#     print(f"Nice to meet you {name}!" )
# greet_with_name("Lida")

#function with more than 1 input
def greet_with(name, location):
    #print(f"Hi {name} from {location}")
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with("Elida","Sarajevo")

# Function with keyword arguments
def greet_with_keyword(name, location):
    #print(f"Hi {name} from {location}")
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with_keyword(name="Elida", location="Sarajevo")