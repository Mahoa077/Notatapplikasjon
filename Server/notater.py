import sqlite3, datetime
from datetime import date

databasekobling = sqlite3.connect("notater.db")
c = databasekobling.cursor()
c.execute("PRAGMA foreign_keys = ON")

c.execute("""
           CREATE TABLE IF NOT EXISTS Inventar(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tittel TEXT NOT NULL,
            innhold TEXT NOT NULL
           )
          """)

def legg_til_notat():
    tittel = input("Skriv inn tittelen på notatet: ")
    innhold = input("Skriv inn teksten som skal være inne i notatet, altså innholdet: ")
    c.execute("INSERT INTO Invetar (tittel, innhold) VALUES (?,?)", (tittel, innhold))
    databasekobling.commit()

def slett_notat():
    notat_id = input("Skriv inn id-en til notatet som skal bli slettet: ")
    c.execute("DELETE FROM Inventar WHERE id = ?", (notat_id))
    databasekobling.commit()

def rediger_notat():
    notat_id = input("Skriv inn id-en til notatet som du vil endre på: ")
    c.execute("SELECT @")