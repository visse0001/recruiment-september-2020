import sqlite3


def read_sqlite_table():
    global sqliteConnection
    try:
        sqliteConnection = sqlite3.connect('../../djangoapp/db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT first_name, last_name, email from auth_user WHERE first_name='sandra'"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print(row)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


read_sqlite_table()
