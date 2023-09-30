import psycopg2
from psycopg2 import Error
from mimesis import Person
from uuid import uuid4 as gid
import json


class database:
    def __init__(self) -> None:
        """база данных"""
        try:
            # Вход в базу данных
            self.database_name = 'postgres'
            self.user_name = 'postgres'
            self.host = 'localhost'
            self.password = 'toor'
            self.connection = psycopg2.connect(
                    user=self.user_name,
                    password=self.password,
                    host=self.host,
                    database=self.database_name
            )
            self.create_table()
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)
            exit()

    def create_table(self) -> None:
        """Создание таблицы"""
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
    
    def add_users(self, id: str, email: str, phone_number: str) -> None:
        """Добовление пользователей в таблицу"""
        self.cursor = self.connection.cursor()
        self.cursor.execute("""INSERT INTO users (id, email, phone_number) VALUES (%s, %s, %s)""", 
                            (str(id), email, phone_number))
        self.connection.commit()

    def system_add_user(self, users: int) -> None:
        """Генерация рандомных пользователей"""
        prs = Person('ru')
        for _ in range(int(users)):
            id = gid()
            email: str = prs.email()
            phone_number: str = prs.phone_number()
            phone_number: str = phone_number.replace('-', ' ')
            self.add_users(id=id, email=email, phone_number=phone_number)
    
    def select_all_users(self) -> list:
        """Экспорт списка всех пользователей"""
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            SELECT id, email, phone_number FROM users
        """)
        result = []
        for i in self.cursor.fetchall():
            user_dict = {'phone_number': i[2]}
            result.append(user_dict)
        return result
        
            


if __name__ == "__main__":
    database().system_add_user(users=100)
    # print(database().select_all_users())
