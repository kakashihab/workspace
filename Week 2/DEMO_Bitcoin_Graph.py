import numpy as np
import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime

tlist = []
alist = []
blist = []

def inf_db():
    con = sqlite3.connect("BitCoinss.db")
    cur = con.cursor()

    cur.execute(
        f"select month, h_price, l_price from currency order by month")
    rows = cur.fetchall()
   
    for row in rows:
        date_str = row[0]
        date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
        d = date_object.strftime("%d %B %Y")
        print(f"{d:20}             {row[1]:-10.2f}   {row[2]:-10.2f}")

        d = date_object.strftime("%y-%m")
        tlist.append(d)
        alist.append(row[1])
        blist.append(row[2])
inf_db()  

alen = len(alist)        
print(f"Length of LIST {alen}")
print(alist)



fig = plt.figure()

x = range(alen)
x = tlist
y = alist
yerr = np.linspace(0.05, 0.2, alen)
plt.errorbar(x, y , yerr=yerr, label='High Value')

blen = len(blist)
# x = range(blen)
x = tlist
y = blist
yerr = np.linspace(0.05, 0.2, blen)
plt.errorbar(x, y , yerr=yerr, label='Low Value')

plt.title('Bitcoin Prices 2020 (06) - 2023 (02)')
plt.ylabel('Value GBP')
plt.xlabel('Year-Month')
plt.legend(loc='upper left')

plt.show()
