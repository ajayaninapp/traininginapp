import sqlite3
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


conn=sqlite3.connect('database.sqlite')
c = conn.cursor()
def season_2015():
    query="SELECT HomeTeam,AwayTeam FROM Matches WHERE season=2015 AND FTHG=5"
    print(pd.read_sql_query(query, conn))
   

def arsenal_loss():
    query="SELECT * FROM Matches WHERE HomeTeam ='Arsenal' AND FTR='A' "
    print(pd.read_sql_query(query, conn))

def bayern_win():
    query="SELECT * FROM Matches WHERE AwayTeam='Bayern Munich' AND FTHG>2 AND Season BETWEEN 2012 AND 2015 "
    print(pd.read_sql_query(query, conn))

def ltr_match():
    query="SELECT * FROM Matches WHERE HomeTeam LIKE 'A%' AND AwayTeam LIKE 'M%'"
    print(pd.read_sql_query(query, conn))

something = False
while not something:
   


    print("1:Print the names of both the Home Teams and Away Teams in each match played in 2015 and Full time Home Goals (FTHG) = 5\n")
    print("2:Print the details of the matches where Arsenal is the Home Team and  Full Time Result (FTR) is “A” (Away Win)\n")
    print("3:Print all the matches from the 2012 season till the 2015 season where Away Team is Bayern Munich and Full time Away Goals (FTHG) > 2\n")
    print("4:Print all the matches where the Home Team name begins with “A” and Away Team name begins with “M”\n")

    a=int(input("Enter choice:\n"))

    if a==1:
        season_2015()
    elif a==2:
        arsenal_loss()
    elif a==3:
        bayern_win()
    elif a==4:
        ltr_match()
    else:
        print("invalid input")
    inout = input('type "y" to continue: ')
    if inout != 'y':
        something = True


conn.close()

