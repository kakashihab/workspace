a = 1

while a <= 12: 
    
    for i in range(1, 13):
        print(a, "x", i, "=", a*i)
    a += 1    

for i in range(1, 13):
    for j in range (1, 13):
        print (f"{i} x {j} = {i * j}")
    print()

