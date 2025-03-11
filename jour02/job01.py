import mysql.connector
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

# Connection to the database (CONST from the .env file)
mydb = mysql.connector.connect(
    host = os.getenv("HOST"),
    user = os.getenv("USER"),
    password = os.getenv("PASS"),
    database="LaPlateforme"
)

# Creation of a cursor
cursor = mydb.cursor()

# Execution of the query to retrieve all students
cursor.execute("SELECT * FROM etudiant")

# Retrieving the results
etudiants = cursor.fetchall()

# Displaying the results
for etudiant in etudiants:
    print(etudiant)

# Closing the cursor and the connection
cursor.close()
mydb.close()