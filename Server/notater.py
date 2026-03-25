from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3, datetime
from datetime import date

app = FastAPI(title="LOTR Notater")

def get_connection():
    return sqlite3.connect("database.db")

with get_connection() as conn:
    cur = conn.cursor()

#databasekobling = sqlite3.connect("database.db",check_same_thread=False)
#c = databasekobling.cursor()
#c.execute("PRAGMA foreign_keys = ON")

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
    c.execute("SELECT * FROM Invetar WHERE id = ?", (notat_id))
    resultat = c.fetchone()
    inn = ""
    tittel = resultat[1]
    innhold = resultat[2]
    while inn != "q" :
        print(f"""
              Hva vil du endre?
              1. Tittel: {tittel}
              2. Innhold: {innhold}
            """)
        inn = input (": ")
        if inn == "1":
            tittel = input("Skriv inn ny tittel: ")
        elif inn == "2":
            innhold = input("Skriv inn nytt innhold: ")
    c.execute("UPDATE Inventar SET tittel = ?, innhold = ? WHERE id =?", (tittel, innhold, notat_id))

    inn = ""
    while inn != "q":
        print("""
              MENY
              1. Legg til notat
              2. Slett notat
              3. Rediger notat
              """)
        inn = input (":")
        match inn:
            case "1":
                legg_til_notat()
            case "2":
                slett_notat()
            case "3":
                rediger_notat()
    c.execute("SELECT * FROM Invetar")
    print(c.fetchall())

    get_connection.commit
    get_connection.close

class Notater(BaseModel):
    tittel: str
    innhold: str

class Todo(BaseModel):
    tittel: str
    oppgaver: list [text:str, done:bool]

#with get_connection() as conn:

@app.get("/notat")
def hent_notat(notat_id: int):
    
     

@app.post("/notater")
def notat(data:Notater):
    print(f"\n\n\n\n\n\nHEI\n\n\n\n\n\n")
    print(data.tittel, data.innhold)
    c.execute("INSERT INTO Inventar (tittel, innhold) VALUES (?,?)", (data.tittel, data.innhold))
    get_connection.commit()


# def get note
# def get note(note_id) 