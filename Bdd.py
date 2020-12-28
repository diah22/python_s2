import sqlite3
try:
    con=sqlite3.connect('db.sqlite')
    cursor= con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                               id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                                name TEXT,
                                age INTEGER)""")


    con.commit()
    print("creation table succeded")
except:

    con.rollback()
    print("creation table failure")

finally:
    con.close()
