import sqlite3

conn = sqlite3.connect("store_trasnactions.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE bitcoin data (
    date text,
    high real,
    low real

)""")

conn.commit()

conn.execute
