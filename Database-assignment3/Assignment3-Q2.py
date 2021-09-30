import sqlite3
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

conn=sqlite3.connect('database.sqlite')
c = conn.cursor()

def count_rows():
    query="SELECT COUNT() FROM TEAMS"
    print(pd.read_sql_query(query, conn))

def seasons():
    query="SELECT DISTINCT Season FROM TEAMS"
    print(pd.read_sql_query(query, conn))

def min_max_capacity():
    query="SELECT MIN(StadiumCapacity),MAX(StadiumCapacity) FROM TEAMS"
    print(pd.read_sql_query(query, conn))

def manu_avg():
    query="SELECT AVG(FTHG) FROM MATCHES WHERE HomeTeam ='Man United' AND Season=2014"
    print(pd.read_sql_query(query, conn))
def squad_sum():
    query="SELECT SUM(KaderHome) FROM Teams WHERE Season=2014"
    print(pd.read_sql_query(query, conn))

something = False
while not something:

    print("1:Counts all the rows in the Teams table\n")
    print("2:Print all the unique values that are included in the Season column in the Teams table\n")
    print("3:Print the largest and smallest stadium capacity that is included in the Teams table\n")
    print("4:Print the sum of squad players for all teams during the 2014 season from the Teams table \n")
    print("5:Query the Matches table to know how many goals did Man United score during home games on average")

    a=int(input("Enter choice:\n"))

    if a==1:
        count_rows()
    elif a==2:
        seasons()
    elif a==3:
        min_max_capacity()
    elif a==4:
        squad_sum()
    elif a==5:
        manu_avg()
    else:
        print("invalid input")
    inout = input('type "y" to continue: ')
    if inout != 'y':
        something = True
    


conn.close()




