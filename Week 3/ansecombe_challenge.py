from matplotlib import pyplot as plt

infile = open("Week 2\dataset1.csv")
x = []
y = []
plt.figure(1) 

for line in infile:
    linevalues = line.rstrip().split(",")
    linelbl = linevalues[0]
    
    xs = float(linevalues[0])
    ys = float(linevalues[1])

    plt.scatter(xs,ys)
  
plt.show()
infile.close()

infile = open("Week 2\dataset2.csv")
x2 = []
y2 = []

for line in infile:
    linevalues = line.rstrip().split(",")
    linelbl = linevalues[0]
    
    xs2 = float(linevalues[0])
    ys2 = float(linevalues[1])

    plt.scatter(xs2,ys2)
   
plt.show()
infile.close()

infile = open("Week 2\dataset3.csv")
x3 = []
y3 = []

for line in infile:
    linevalues = line.rstrip().split(",")
    linelbl = linevalues[0]
    
    xs3 = float(linevalues[0])
    ys3 = float(linevalues[1])

    plt.scatter(xs3,ys3)
  
plt.show()
infile.close()

infile = open("Week 2\dataset4.csv")
x4 = []
y4 = []

for line in infile:
    linevalues = line.rstrip().split(",")
    linelbl = linevalues[0]
    
    xs4 = float(linevalues[0])
    ys4 = float(linevalues[1])

    plt.scatter(xs4,ys4)
    

plt.show()
infile.close()


