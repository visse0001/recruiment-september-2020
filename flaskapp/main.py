import sqlite3

from flask import Flask, request

app = Flask(__name__)


def read_sqlite_table(first_name, last_name, email):
    try:
        sqliteConnection = sqlite3.connect('../djangoapp/db.sqlite3')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT first_name, last_name, email 
                                    FROM auth_user 
                                    WHERE first_name=first_name 
                                    AND last_name=last_name 
                                    AND email=email
                                    """
        cursor.execute(sqlite_select_query)
        record = cursor.fetchone()
        cursor.close()

        return record

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


@app.route("/check", methods=["GET", "POST"])
def hello():
    content = request.get_json(force=True)
    first_name = content['first_name']
    last_name = content['last_name']
    email = content['email']

    user = read_sqlite_table(first_name, last_name, email)
    if len(user) > 0:
        return 'PASS'
    return 'FAIL'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
