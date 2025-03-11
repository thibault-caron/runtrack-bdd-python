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

    # Create a cursor to execute SQL queries
    cursor = mydb.cursor()



    # Close the cursor
    cursor.close()

# Close the connection
mydb.close()