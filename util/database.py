import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared

class Database:

    cursor = None
    mydb = None 

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            )
        
        self.cursor = self.mydb.cursor()
        #Checking if the database already exists
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS coinflip")
        #Making cursor only access coinflip
        self.cursor.execute("USE coinflip")
        #creating login table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS login (username VARCHAR(100), password VARCHAR(100))")
        

        
    def add_login(self,username,password):
        prepared_statement = "INSERT INTO login (username, password) VALUES (%s, %s)"
        values = (username, password)
        #inserts values into the prepared statement
        self.cursor.execute(prepared_statement,values)
        self.mydb.commit()


#just testing to see if values are added
def test1():
        db = Database()
        db.add_login("dinulawe", "dinulawe.1")
        db.add_login("mthamilv", "mthamilv.1")
        db.add_login("cpena3", "cpena3.1")
        db.add_login("gpdavis", "gpdavis.1")
        db.add_login("joshanef", "joshanef.1")

if __name__ == "__main__":
     test1()
        