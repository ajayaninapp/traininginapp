class Car:
    def __init__(self,carname,owner) :
        self.carname=carname
        self.owner=owner

import sqlite3


conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE cars (
            carname text,
            owner text)""")

def insert_car(car):
    with conn:
        c.execute("INSERT INTO cars VALUES (:carname, :owner)", {'carname': car.carname, 'owner': car.owner, })

def get_list():
    c.execute("SELECT * FROM cars")
    return c.fetchall()


for i in range(0,9):
    newcar=Car('','')
    newcar.carname=input("Enter carname ------->\t")
    newcar.owner=input("owner name -------->\t")
    insert_car(newcar)
    



allcars = get_list()
print("Car name:\t\t\tOwner\n")
for item in allcars:
    print(f"{item[0]}\t\t\t\t{item[1]}")


