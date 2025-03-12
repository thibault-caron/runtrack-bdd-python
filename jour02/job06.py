import mysql.connector
import os  # importing os module for environment variables
from dotenv import load_dotenv  # importing necessary functions from dotenv library

load_dotenv()  # loading variables from .env file

try: 
    # Connection to the database
    mydb = mysql.connector.connect(
        host = os.getenv("HOST"),
        user = os.getenv("USER"),
        password = os.getenv("PASS"),
        database="LaPlateforme"
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT SUM(capacite) FROM salle")
    result = cursor.fetchone()

    capacite_totale = int(result[0]) if result[0] is not None else 0

    print(f'La capacité de toutes les salles est de : {capacite_totale} personnes')

except mysql.connect.Error as error: 
    print(f'Error occurred: {error}')

finally: 
    cursor.close()
    mydb.close()