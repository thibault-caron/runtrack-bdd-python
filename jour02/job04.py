import mysql.connector
import os  # importing os module for environment variables
from dotenv import load_dotenv  # importing necessary functions from dotenv library

load_dotenv()  # loading variables from .env file


# Connection to the database
mydb = mysql.connector.connect(
    host = os.getenv("HOST"),
    user = os.getenv("USER"),
    password = os.getenv("PASS"),
    database="LaPlateforme"
)

if mydb.is_connected():
   
    db_info = mydb.get_server_info()
    print(f"Connected to MySQL, version: {db_info}")

    cursor = mydb.cursor()
    cursor.execute("SELECT nom, capacite FROM salle")
    results = cursor.fetchall()

    # Display the result in the console
    print("List of rooms and their capacities:")
    for row in results:
        print(f"Name: {row[0]}, Capacity: {row[1]}")

    cursor.close()

mydb.close()