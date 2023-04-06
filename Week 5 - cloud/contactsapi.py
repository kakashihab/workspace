from fastapi import FastAPI
import pymysql
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    firstname : str
    lastname : str
    email : str
    city : str
    phonenumber : int

@app.get("/contacts")
def api_get_contacts(name : str = ""):
    #connect to db
    con= pymysql.connect(host="localhost", user="root", password="root123", database="onlinestore")
    cur = con.cursor()

    #query the db
    if name == "":
        sql = "select * from contacts"
    else:
        sql = f"select * from contacts where first_name = '{name}'"
    
    cur.execute(sql)
    res = cur.fetchall()
   

    #close connection
    cur.close()
    con.close()

    #format the results
    l = []
    
    for names in res:
        d = {"first_name:": names[1],
             "last_name" : names[2],
             "email" : names[3],
             "city" : names[4],
             "phonenum" : names[5]}
        
        l.append(d)
    return l

@app.post("/contacts")
def api_post_contact(user : User):
    #connect to db
    con= pymysql.connect(host="localhost", user="root", password="root123", database="onlinestore")
    cur = con.cursor()

    #run query
    sql = "insert into contacts(first_name, last_name, email, city, phonenum) values('{user.firstname}','{user.lastname}','{user.email}','{user.city}',{user.phonenumber})"
    cur.execute(sql)
    con.commit()


    #close connection
    cur.close()
    con.close()

    #retunr message 
    return {"message" : "inserted",
            "message" : "inserted",
            "message" : "inserted",
            "message" : "inserted",
            "message" : "inserted"}
    


    