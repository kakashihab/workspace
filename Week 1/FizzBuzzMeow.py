#Write a fizzbuzz challenge 

for a in range(200):
    
    if a % 7 == 0 and a % 3 == 0 and a % 5 == 0:
        print("FizzBuzzMeow")

    elif a % 3 == 0 and a % 5 == 0:
        print("FizzBuzz")
      
    elif a % 5 ==0:
        print("Buzz")
       
    elif a % 3 == 0:
        print("Fizz")

    elif a % 7 == 0:
        print("Meow")
              
    else: 
        print(a)