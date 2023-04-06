from matplotlib import pyplot as plt

infile = open("states_info_edit.csv")

for line in infile:
    linevalues = line.rstrip().split(",")
    linelbl = linevalues[0]
    linevalues.pop(0)
    
    #linevalues.reverse()
    for i in range(0, len(linevalues)):
        linevalues[i] = int(linevalues[i])
    print(linevalues)

    plt.plot(years, linevalues, linestyle="solid", label=linelbl)
    plt.legend()

plt.show()
infile.close()

plt.scatter(widgets, gromits)

plt.xlabel("Widgets")
plt.ylabel("Gromits")
plt.title("Widgets and Gromits")
plt.show()