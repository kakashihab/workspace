l = [0, 1, 2, 3, 4]

try:
    outfile = open("numbers.txt.", "w")
    for i in range(0, 9):
        print(l[i], file=outfile)
    outfile.close()

except PermissionError:
    print("you are not allowed to write to this file")

print("Finished")
