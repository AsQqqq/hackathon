import psycopg2
from psycopg2 import Error
from mimesis import Person
from uuid import uuid4 as gid
import json


class database:
    def __init__(self) -> None:
        """база данных"""
        try:
            self.database_name = 'hackathon'
            self.user_name = 'hackathon'
            self.host = 'localhost'
            self.password = 'toor'
            self.connection = psycopg2.connect(
                    user=self.user_name,
                    password=self.password,
                    host=self.host,
                    database=self.database_name
            )
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()
            print("You are connected to - ", record, "\n")
            self.create_table()
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if (self.connection):
                self.cursor.close()
                self.connection.close()
                print("PostgreSQL connection is closed")
    
    def create_table(self) -> None:
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                sequence_number SERIAL PRIMARY KEY,
                id TEXT,
                email TEXT,
                phone_number TEXT
            )
        """)
        self.connection.commit()
    
    def add_users(id: str, phone_number: int, email: str) -> None:
        pass

    def system_add_user(self, users: int) -> None:
        """Добовление пользователей в базу данных(рандомных)"""
        prs = Person('ru')

        for _ in range(int(users)):
            id = gid()
            phone_number = prs.phone_number()
            email = prs.email()
            
            print("\n\n")
            print(id)
            print(phone_number.replace('-', ' '))
            print(email)
            print("\n\n")
            


if __name__ == "__main__":
    database().system_add_user(users=100)
            