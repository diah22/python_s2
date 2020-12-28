import sqlite3
try:
    con=sqlite3.connect('db.sqlite')
    cursor= con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
                               idcli INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                                nom TEXT,
                                prenom TEXT, 
                                cincli TEXT
                                agecli INTEGER)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS bedroom(
                                numCh INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                                typeCh TEXT,
                                etach TEXT,
                                disponibiliteCh TEXT,
                                prixCh DOUBLE)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS booking(
                                   idRes INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                                   date_entree DATE,
                                   date_sortie DATE,
                                   prix_Res DOUBLE,
                                   idcli INTEGER)""")
    con.commit()
    print("creation table succeded")
except:

    con.rollback()
    print("creation table failure")

finally:
    con.close()
