from fastapi import FastAPI
import pymysql
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    make : str
    model : str
    colour : str
    year : str
    license_plate : str
    location : str
    purchasefrom : str
    purchaseprice : str
    sellingprice : str
    


@app.get("/getCarDetails")
def api_get_newcar(car: str = ""):
    #connect to db
    con = pymysql.connect(host="localhost", user="root", password="root123", database="cars")
    cur = con.cursor()

    #query the db
    if car == "":
        sql = "select * from our_cars"
    else: 
        sql = f"select * from ourcars where make = '{car}'"

    cur.execute(sql)
    res = cur.fetchall()

    #close connection
    cur.close()
    con.close()

    #format results
    c = []

    for cars in res:
        data = {"make:" : car[1],
                "model:" : car[2],
                "colour:" : car[3],
                "year:" : car[4],
                "license_plate:" : car[5],
                "location:" : car[6],
                "purchased_from:" : car[7],
                "purchase_price:" : car[8],
                "selling_price:" : car[9]}
        c.append(data)
    return c

@app.post("/addNewCar") 
def api_post_contact(addcar : User):

    #connect to db
    con = pymysql.connect(host="localhost", user="root", password="root123", database="cars")
    cur = con.cursor()   

    #run query 
    sql = "insert into our_cars(make, model, colour, year, license_plate, location, purcased_from, purchase_price, selling_price) values({addcar.make}','{addcar.model}','{addcar.colour}','{addcar.year}','{addcar.license_plate}','{addcar.location}','{addcar.purchasefrom}','{addcar.purchaseprice}','{addcar.sellingprice})"   
    cur.execute(sql)
    con.commit()


    #close connection
    cur.close()
    con.close()

    #return message
    return {"message" : "inserted",
            "message" : "inserted",
            "message" : "inserted",
            "message" : "inserted",
            "message" : "inserted",
            "message" : "inserted",
            "message" : "inserted",
            "message" : "inserted",
            "message" : "inserted"}


