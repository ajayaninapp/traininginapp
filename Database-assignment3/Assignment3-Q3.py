import sqlite3
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


conn=sqlite3.connect('database.sqlite')
c = conn.cursor()

def games_won():
    query="SELECT HomeTeam,COUNT(Match_ID) AS Games_Won FROM Matches WHERE Season=2016 AND FTR='H' GROUP BY HomeTeam ORDER BY COUNT(Match_ID) DESC"
    print(pd.read_sql_query(query, conn))
    


def aachen_details():
    query="SELECT HomeTeam,FTHG,FTAG FROM Matches WHERE HomeTeam='Aachen'AND Season=2010 ORDER BY FTHG DESC"
    print(pd.read_sql_query(query, conn))
    
def ten_records():
    query="SELECT * FROM Unique_Teams LIMIT 10"
    print(pd.read_sql_query(query, conn))
def team_join():
    query="SELECT * From Teams Join Unique_Teams ON (Unique_Teams.TeamName=Teams.TeamName) LIMIT 10"
    print(pd.read_sql_query(query, conn))
def team_join2():
    query="SELECT  Unique_Teams.Unique_Team_ID,Unique_Teams.TeamName,Teams.AvgAgeHome,Teams.Season,Teams.ForeignPlayersHome From Teams Join Unique_Teams ON (Unique_Teams.TeamName=Teams.TeamName) LIMIT 5"
    print(pd.read_sql_query(query, conn))

def max_matchid():
    query="""SELECT MAX(Teams_in_Matches.Match_ID) AS Max_matchid,Unique_Teams.Unique_Team_ID,Unique_Teams.TeamName FROM Teams_in_Matches,Unique_Teams
     WHERE (Unique_Teams.Unique_Team_ID=Teams_in_Matches.Unique_Team_ID)AND (Unique_Teams.TeamName LIKE '%y' OR Unique_Teams.TeamName LIKE '%r')
     GROUP BY Unique_Teams.Unique_Team_ID"""
    print(pd.read_sql_query(query, conn))


def using_where():
    query="""SELECT  Teams_in_Matches.Match_ID ,Teams_in_Matches.Unique_Team_ID,Unique_Teams.TeamName 
            FROM Teams_in_Matches,Unique_Teams
            WHERE Teams_in_Matches.Unique_Team_ID=Unique_Teams.Unique_Team_ID
            LIMIT 30
           
           """
    print(pd.read_sql_query(query, conn))
def using_join():
    query="""SELECT  Teams_in_Matches.Match_ID ,Teams_in_Matches.Unique_Team_ID,Unique_Teams.TeamName 
            FROM Teams_in_Matches
            JOIN Unique_Teams ON Teams_in_Matches.Unique_Team_ID=Unique_Teams.Unique_Team_ID
            LIMIT 30
           
           """
    print(pd.read_sql_query(query, conn))

something = False
while not something:

    print("1:Query that returns the HomeTeam, FTHG (number of home goals scored in a game) and FTAG.....\n")
    print("2Print the total number of home games each team won during the 2016 season in descending order of number of home games from the Matches table.\n")
    print("3:Write a query that returns the first ten rows from the Unique_Teams table\n")
    print("4:Print Match id and Team name using where\n")
    print("5:Print Match id and Team name using join\n")
    print("6:Join Unique_teams and Teams_table(10 rows)\n")
    print("7: Query that shows the Unique_Team_ID and TeamName from the Unique_Teams table and AvgAgeHome, Season and ForeignPlayersHome from the Teams table(5 rows)\n")
    print("8: Query that shows the highest Match_ID for each team that ends in a “y” or a “r\n")

    a=int(input("Enter choice:\n"))

    if a==1:
        aachen_details()
    elif a==2:
        games_won()
    elif a==3:
        ten_records()
    elif a==4:
        using_where()
    elif a==5:
        using_join()
    elif a==6:
        team_join()
    elif a==7:
        team_join2()
    elif a==8:
        max_matchid()
    else:
        print("invalid input")

    inout = input('type "y" to continue: ')
    if inout != 'y':
            something = True


conn.close()
