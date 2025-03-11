import mysql.connector
import os  # importing os module for environment variables
from dotenv import load_dotenv  # importing necessary functions from dotenv library

load_dotenv()  # loading variables from .env file

# Connection to the database (CONST from the .env file)
mydb = mysql.connector.connect(
    host = os.getenv("HOST"),
    user = os.getenv("USER"),
    password = os.getenv("PASS"),
    database="LaPlateforme"
)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM etudiant")
etudiants = cursor.fetchall()

# Displaying the results
for etudiant in etudiants:
    print(etudiant)

cursor.close()
mydb.close()