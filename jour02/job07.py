from database import Database

class Employe(Database):
    def __init__(self):
        super().__init__("HumanRessourcesJ2")

    def create(self, nom, prenom, salaire, id_service):
        query = f"INSERT INTO employe (nom, prenom, salaire, Id_service) VALUES ('{nom}', '{prenom}', {salaire}, {id_service})"
        self.execute_query(query)
        self.mydb.commit()

    def read(self, id_employe):
        query = f"SELECT * FROM employe WHERE Id_employe = {id_employe}"
        return self.execute_query(query)

    def update(self, id_employe, nom=None, prenom=None, salaire=None, id_service=None):
        updates = []
        if nom:
            updates.append(f"nom = '{nom}'")
        if prenom:
            updates.append(f"prenom = '{prenom}'")
        if salaire:
            updates.append(f"salaire = {salaire}")
        if id_service:
            updates.append(f"Id_service = {id_service}")
        updates_str = ", ".join(updates)
        query = f"UPDATE employe SET {updates_str} WHERE Id_employe = {id_employe}"
        self.execute_query(query)
        self.mydb.commit()

    def delete(self, id_employe):
        query = f"DELETE FROM employe WHERE Id_employe = {id_employe}"
        self.execute_query(query)
        self.mydb.commit()

class Service(Database):
    def __init__(self):
        super().__init__("HumanRessourcesJ2")

    def create(self, nom):
        query = f"INSERT INTO service (nom) VALUES ('{nom}')"
        self.execute_query(query)
        self.mydb.commit()

    def read(self, id_service):
        query = f"SELECT * FROM service WHERE Id_service = {id_service}"
        return self.execute_query(query)

    def update(self, id_service, nom):
        query = f"UPDATE service SET nom = '{nom}' WHERE Id_service = {id_service}"
        self.execute_query(query)
        self.mydb.commit()

    def delete(self, id_service):
        query = f"DELETE FROM service WHERE Id_service = {id_service}"
        self.execute_query(query)
        self.mydb.commit()

if __name__ == "__main__":
    employe = Employe()
    service = Service()

    # Create
    # service.create("Informatique")
    # employe.create("Doe", "John", 1000, 1)

    # Read
    print(employe.read(2))
    print(service.read(1))

    # Update
    employe.update(2, nom="Doe", prenom="Jane", salaire=1500, id_service=1)
    print(employe.read(2))
    # service.update(1, nom="HR")
    # print(service.read(1))

    # Delete
    # employe.delete(1)
    # service.delete(1)

    employe.close()
    service.close()