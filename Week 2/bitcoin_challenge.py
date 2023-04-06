import requests
import json
import sqlite3

con = sqlite3.connect("bitcoin.db")
cur = con.cursor()

def database():

    url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_MONTHLY&symbol=BTC&market=GBP&apikey=80c930c817f54a033a6aedfac1aaa0fa"

    res = requests.get(url)
    resdec = res.content.decode("utf-8")
    datacollection = json.loads(resdec)

    print(res.status_code)

    cur.execute("CREATE TABLE IF NOT EXISTS bitcoin (month, high, low)")


    json_key = "Time Series (Digital Currency Monthly)"
    month_key = "2a. high (GBP)"
    month_key_low = "3a. low (GBP)"

    for month in datacollection[json_key]:
        #print(month)
        monthly_data = datacollection[json_key][month]
        cur.execute(f"INSERT INTO bitcoin (month, high, low) VALUES ('{month}', {monthly_data[month_key]}, {monthly_data[month_key_low]})")
        con.commit()

    con.commit()

database()

cur.execute("select month, max(high) from bitcoin")
high = cur.fetchall()
cur.execute("select month, min(low) from bitcoin")
low = cur.fetchall()

user_ask = input("What year would you like to search? ")
query = f"select month, max(high) from bitcoin where month like '%{user_ask}%'"
highest = cur.execute(query)
data = cur.fetchall()
print(data)
lowest = cur.execute(f"select month, min(low) from bitcoin where month like '%{user_ask}%'")
data = cur.fetchall()
print(data)

