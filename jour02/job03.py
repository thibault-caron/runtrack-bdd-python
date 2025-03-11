import mysql.connector
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv
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

# Query to add datas in etage
query_etage = """
INSERT INTO etage (nom, numero, superficie) 
VALUES 
('RDC', 0, 500), 
('R+1', 1, 500);
"""
cursor.execute(query_etage)
print(query_etage)

# Query to add datas in salle
query_salle = """
INSERT INTO salle (nom, id_etage, capacite) 
VALUES 
('Lounge', 1, 100), 
('Studio Son', 1, 5), 
('Broadcasting', 2, 50), 
('Bocal Peda', 2, 4), 
('Coworking', 2, 80), 
('Studio Video', 2, 5);
"""
cursor.execute(query_salle)
print(query_salle)

# Verify that datas have been added properly
cursor.execute("SELECT * FROM etage")
print("Table 'etage':", cursor.fetchall())

cursor.execute("SELECT * FROM salle")
print("Table 'salle':", cursor.fetchall())

mydb.commit()

cursor.close()
mydb.close()


# mysqldump -u root -p LaPlateforme > laplateforme_jour02_job03.sql

# mysqldump -u root -p LaPlateforme --result-file=laplateforme_jour02_job03.sql
