#Task 1: Write a program that requests the user to enter a word or phrase Display the string as it was entered then in uppercase then in lowercase then display the length of the string : The string has 10 characters then display the string with spaces
print("Starting Task 1")
car_brand = input("Type a make of a car: ")
print(car_brand)
print(car_brand.upper())
print(car_brand.lower())
print(f"The string has {len(car_brand)} characters")
print(car_brand.replace(" ", ""))


#Task 2 create a phrasal template (mad lib)
print("Starting Task 2")
user_gender = input("What gender are you? ")
user_name = input("Please enter your name: ")
user_scared = input("What would you scream if you saw Michael Myers?")

print(f"There once was a {user_gender} who was called {user_name} \
they were running down the hallway when they came across Michael Myer, once they saw him they screamed {user_scared.upper()}")