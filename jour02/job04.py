import mysql.connector
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv
# loading variables from .env file
load_dotenv() 


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

    # Execute the SQL query to retrieve room names and capacities
    cursor.execute("SELECT nom, capacite FROM salle")

    # Retrieve all results
    results = cursor.fetchall()

    # Display the result in the console
    print("List of rooms and their capacities:")
    for row in results:
        print(f"Name: {row[0]}, Capacity: {row[1]}")

    # Close the cursor
    cursor.close()

# Close the connection
mydb.close()