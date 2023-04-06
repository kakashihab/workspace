from datetime import datetime

# presidents dictionary
# "name": [Date of birth(Y, M, D), Year of Marriage(Y, M, D)]
presidents = {
    "Lyndon B Johnson": [(1908, 8, 27), (1934, 10, 17)],
    "Richard Nixon": [(1913, 1, 9), (1940, 6, 21)],
    "Gerald Ford": [(1913, 7, 14), (1948, 10, 15)],
    "Jimmy Carter": [(1924, 10, 1), (1946, 7, 7)],
    "Ronald Reagan": [(1911, 2, 6), (1940, 1, 26)],
    "George H W Bush": [(1924, 6, 12), (1945, 1, 6)],
    "Bill Clinton": [(1946, 8, 19), (1975, 10, 11)],
    "George W Bush": [(1946, 7, 6), (1977, 11, 5)],
    "Barack Obama": [(1961, 8, 4), (1992, 10, 3)],
    "Donald Trump": [(1946, 6, 14), (1977, 4, 7)],
    "Joe Biden": [(1942, 11, 20), (1966, 8, 27)],
}

# List of solomon grundy president names
solomons = []

# Loop over each president
for president in presidents:
    # Convert date of birth tuple into datetime
    dob = datetime(*presidents[president][0])

    # Check if born on a monday and add to monday string
    monday = ""
    if dob.weekday() == 0:
        monday = ": born on a Monday"

    # Check if born on a wednesday and add to wednesday string
    marriage = datetime(*presidents[president][1])
    wednesday = ""
    if marriage.weekday() == 2:
        wednesday = ": married on a Wednesday"

    # if born on a monday and married on a wednesday add to solomons list
    if monday and wednesday:
        solomons.append(president)

    print(f"{president} : {dob.strftime('%d %B %Y')} {monday} {wednesday}")

print(f"\nThere are {len(solomons)} Solomon Grundy presidents")
if solomons:
    for solomon in solomons:
        print(f"{solomon} is a Solomon Grundy")