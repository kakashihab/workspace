import json

# create a string that contains some json
s = """
    [
        {
            "make": "Ford",
            "model": "Fiesta",
            "colour": "red",
            "registration": "AB01 2BC"
        },
        {
            "make": "Vauxhall",
            "model": "Corsa",
            "colour": "black",
            "registration": "BC01 3BD"
        },
        {
            "make": "Volkswagen",
            "model": "Beetle",
            "colour": "yellow",
            "registration": "DE01 4BD"
        }
    ]
"""

print(s)
print(type(s))
print("----------------------")

# convert the string into a list using json.loads
cars = json.loads(s)
print(cars)
print(type(cars))

for car in cars:
    print(car["make"], car["model"])

# write the list out to a file using json.dump
outfile = open("cars.json", "w")
json.dump(cars, outfile)
outfile.close()
print("----------------------")

# create a dictionary
mynewcar = {
                "make": "Audi",
                "model": "A4",
                "colour": "blue",
                "registration": "FF99 GG99"
            }

print(mynewcar)
print(type(mynewcar))

# convert the dictionary into a string using json.dumps
carstring = json.dumps(mynewcar)
print(carstring)
print(type(carstring))


# read values from a file into a list using json.load this is from Colin's files 
infile = open("infile.json")
fruits = json.load(infile)
infile.close()

print(type(fruits))

for fruit in fruits:
    print(fruit["name"], fruit["qty"])