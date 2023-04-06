#a = input("Type something: ")
#print("You typed: " + a + ", which was a good thing to type.") #concatenate strings
#print(f"you typed: {a}, which is really good to type") #f string better way to connect strings (easier to the eye too)
#print(type(a)) #checks what type/variable is assigned 
#print(len(a))
#print(a.replace("l", "g"))

total = 20

if total == 100:
    print("Total is 100")
elif total == 10:
    print("total is 10")
elif total == 20: 
    print("Total is 20")
else:
    print("total is not 100")

r = range(20, 5, -3)

for a in r:
    print(a)