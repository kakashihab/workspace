import sqlite3
import csv

con = sqlite3.connect("books.db")
cur = con.cursor()

cur.execute("create table if not exists books (title text, author text)")
cur.execute("delete from books")
con.commit()

cur.execute("insert into books values('War and Peace', 'Tolstoy, Leo')")
cur.execute("insert into books values('Pride and Prejudice', 'Austen, Jane')")
cur.execute("insert into books values('Great Expectations', 'Dickens, Charles')")

bookdata = [("Jude the Obscure", "Hardu, Thomas"),
            ("Middlemarch", "Eliot, George"),
            ("Animal Farm", "Orwell, George")]
cur.executemany("insert into books values(?, ?)", bookdata)
con.commit()

infile = open("books.db")
for line in csv.reader(infile, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
    cur.execute("insert into books values(?, ?)", line)
infile.close()
con.commit()

cur.execute("delete from books where author = 'Orwell, George'")
cur.execute("select * from books")
res = cur.fetchall()
con.commit()
print(res)

cur.execute("select * from books")
res = cur.fetchall()

print(res)

connection = sqlite3.connect("books.db")
cursor = connection.cursor()

author = input("please enter an author name: ")
search = (f"select * from books where author like '%{author}%'")
cursor.execute(search)
ans = cursor.fetchall()
print(ans)

con.close()