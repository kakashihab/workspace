from datetime import datetime, timedelta

president = {"Lyndon B Johnson" : (1908, 8, 27), 
             "Richard Nixon" : (1913, 1, 9),
             "Gerald Ford" : (1913, 7, 14),
             "Jimmy Carter" : (1924, 10, 1),
             "Ronald Reagan" : (1911, 2, 6),
             "George H W Bush" : (1924, 6, 12),
             "Bill Clinton" : (1946, 8, 19),
             "George W Bush" : (1946, 7, 6),
             "Barrack Obama" : (1961, 8, 4),
             "Donald Trump" : (1946, 6, 14),
             "Joe Biden" : (1942, 11, 20)}



for i in president:
    dob = datetime(*president[i])

    #d = dob.weekday()
    dayofbirth = (dob.strftime("%A"))
    print(f"{i} was born on a {dayofbirth}")

wedding = {    "Lyndon B. Johnson": (1934, 10, 17),
               "Richard Nixon": (1940, 6, 21),
               "Gerald Ford": (1948, 10, 15),
               "Jimmy Carter": (1946, 7, 7),
               "Ronald Reagan": (1940, 1, 26),
               "George H.W. Bush": (1945, 1, 6),
               "Bill Clinton": (1975, 10, 11),
               "George W. Bush": (1977, 11, 5),
               "Barack Obama": (1992, 10, 3),
               "Donald Trump": (1977, 4, 7),
               "Joe Biden": (1966, 8, 27)
}

#for loop to check number of presidents that got married and what day it was. 
for n in wedding:
    dom = datetime(*wedding[n])

    #m = dom.weekday() 
    dayofmarriage = (dom.strftime("%A"))
    print(f"{n} married on {dayofmarriage}")


if i == 0 and n == 2:
    print(f"{i}Are solomon grundys")
else:
    print("There are no solomon Grundys")


#print(president["Barrack Obama"])
#w = president

#for president in president:
   # d = datetime(*president)
   # d.weekday()
