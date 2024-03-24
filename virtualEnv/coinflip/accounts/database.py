import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared

class Database:
    cursor = None
    mydb = None

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
        )
        self.cursor = self.mydb.cursor()
        # Checking if the database already exists
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS coinflip")
        # Making cursor only access coinflip
        self.cursor.execute("USE coinflip")
        # Creating login table
        self.cursor.execute("CREATE TABLE IF NOT EXISTS login (username VARCHAR(100), password VARCHAR(100))")

    def add_login(self, username, password):
        prepared_statement = "INSERT INTO login (username, password) VALUES (%s, %s)"
        values = (username, password)
        # Inserts values into the prepared statement
        self.cursor.execute(prepared_statement, values)
        self.mydb.commit()

    def valid_login(self, username, password):
        prepared_statement = "SELECT password FROM login WHERE username = %s"
        value = (username,)
        self.cursor.execute(prepared_statement, value)
        result = self.cursor.fetchall()
        # If the result is false, that means the username is incorrect
        if len(result) == 0:
            return False
        pw_in_table = result[0][0]
        # If the result is the wrong password
        if pw_in_table != password:
            return False
        # If the result is the correct password
        elif pw_in_table == password:
            return True

# Just testing to see if values are added
def test1():
    db = Database()
    db.add_login("dinulawe", "dinulawe.1")
    db.add_login("mthamilv", "mthamilv.1")
    db.add_login("cpena3", "cpena3.1")
    db.add_login("gpdavis", "gpdavis.1")
    db.add_login("joshanef", "joshanef.1")

# Checking to see if it retrieves an existing login with both correct values
def test2():
    db = Database()
    result = db.valid_login("dinulawe", "dinulawe.1")
    assert result == True

# Checking to see if it returns false if the username is incorrect
def test3():
    db = Database()
    result = db.valid_login("dinulaw", "dinulawe.1")
    assert result == False

# Checking to see if it returns false if the password is incorrect
def test4():
    db = Database()
    result = db.valid_login("dinulawe", "dinulawe")
    assert result == False

if __name__ == "__main__":
    # test1()
    test2()
    test3()
    test4()