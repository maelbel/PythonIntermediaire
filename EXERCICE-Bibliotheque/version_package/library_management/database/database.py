import sqlite3

DATABASE_PATH = 'Cas_pratique_bibliotheque/version_package/library_management/database/db.sqlite3'

def create_users(DATABASE_PATH:str) -> None:
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        nom VARCHAR(30) NOT NULL,
        prenom varchar(30) NOT NULL
    )
    """)
        sql = "INSERT INTO users values(NULL, :nom, :prenom)"
        user1_data = {"nom": "Berger", "prenom": "Michel"}
        user2_data = {"nom": "Belliard", "prenom": "Mael"}
        
        cursor.execute(sql, user1_data)
        cursor.execute(sql, user2_data)

        conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

def create_books(DATABASE_PATH:str) -> None:
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        title VARCHAR(30) NOT NULL,
        author varchar(30) NOT NULL
    )
    """)
        sql = "INSERT INTO books values(NULL, :title, :author)"
        book1_data = {"title": "Pensées pour moi-même", "author": "Marc-Aurèle"}
        book2_data = {"title": "Le Cid", "author": "Corneille"}
        
        cursor.execute(sql, book1_data)
        cursor.execute(sql, book2_data)

        conn.commit()

    except Exception as e:
        print(e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

def create_loans(DATABASE_PATH:str) -> None:
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute("""
    CREATE TABLE IF NOT EXISTS loans(
        id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        user_id int NOT NULL,
        book_id int NOT NULL
    )
    """)
        conn.commit()
        
    except Exception as e:
        print(e)
        conn.rollback()

    finally:
        cursor.close()
        conn.close()

def create_db() -> None:
    try:

        create_users(DATABASE_PATH)
        create_books(DATABASE_PATH)
        create_loans(DATABASE_PATH)

    except Exception as e:
        print(e)

    finally:
        print("Database created...")
