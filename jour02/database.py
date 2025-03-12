import mysql.connector
import os  # importing os module for environment variables
from dotenv import load_dotenv  # importing necessary functions from dotenv library

load_dotenv()  # loading variables from .env file

class Database:
    def __init__(self, database_name="LaPlateforme"):
        try: 
            self.mydb = mysql.connector.connect(
                host = os.getenv("HOST"),
                user = os.getenv("USER"),
                password = os.getenv("PASS"),
                database=database_name
            )
            self.cursor = self.mydb.cursor()
        
        except mysql.connect.Error as error:
            print(f'Error occurred: {error}')

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.mydb.close()

    def create(self, table, data):
        placeholders = ', '.join(['%s'] * len(data))
        columns = ', '.join(data.keys())
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(sql, list(data.values()))
        self.mydb.commit()
        return self.cursor.lastrowid

    def read(self, table, where=None):
        sql = f"SELECT * FROM {table}"
        if where:
            sql += " WHERE " + ' AND '.join([f"{k}=%s" for k in where.keys()])
            self.cursor.execute(sql, list(where.values()))
        else:
            self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update(self, table, data, where):
        set_clause = ', '.join([f"{k}=%s" for k in data.keys()])
        where_clause = ' AND '.join([f"{k}=%s" for k in where.keys()])
        sql = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        self.cursor.execute(sql, list(data.values()) + list(where.values()))
        self.mydb.commit()
        return self.cursor.rowcount

    def delete(self, table, where):
        where_clause = ' AND '.join([f"{k}=%s" for k in where.keys()])
        sql = f"DELETE FROM {table} WHERE {where_clause}"
        self.cursor.execute(sql, list(where.values()))
        self.mydb.commit()
        return self.cursor.rowcount