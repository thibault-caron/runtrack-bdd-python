import mysql.connector
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 


# Connexion à la base de données
mydb = mysql.connector.connect(
    host = os.getenv("HOST"),
    user = os.getenv("USER"),
    password = os.getenv("PASS"),
    database="LaPlateforme"
)

# Création d'un curseur
cursor = mydb.cursor()