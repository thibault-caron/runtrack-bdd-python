CREATE DATABASE HumanRessourcesJ2;
SHOW DATABASES;

CREATE TABLE service(
   Id_service INT AUTO_INCREMENT,
   nom VARCHAR(50) NOT NULL,
   PRIMARY KEY(Id_service)
);

CREATE TABLE employe(
   Id_employe INT AUTO_INCREMENT,
   nom VARCHAR(50) NOT NULL,
   prenom VARCHAR(50) NOT NULL,
   salaire DECIMAL(10,2) NOT NULL,
   Id_service INT NOT NULL,
   PRIMARY KEY(Id_employe),
   FOREIGN KEY(Id_service) REFERENCES service(Id_service)
);
SHOW TABLES;
DESCRIBE employe;