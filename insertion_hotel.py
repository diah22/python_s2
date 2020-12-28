import sqlite3
i=0
nbnom=int(input("combien de nom voulez vous inserez? :"))
while(i<nbnom):
    nom=input('entre un nom')
    age=input('entrer l age')
    try:
        con = sqlite3.connect('db.sqlite')
        cursor = con.cursor()
        cursor.execute("""INSERT INTO users(name, age) VALUES (?,?)""",
                       (nom, age))
        print("Insertion donnee avec succes")
        cursor.execute("""SELECT id, name, age FROM users""")
        
        i=i+1
        print("recuperation de tous les donnees dans le table")
        for row in cursor:
            print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
    except:
        print("data insertion failure, may be your table is not created")
        con.rollback()

con.close()