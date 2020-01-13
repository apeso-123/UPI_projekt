import sqlite3
import os, sys

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/Entiteti/')

from drzava import Drzava

def unesi_demo_podatke():
    conn = sqlite3.connect("upi_projekt.db")

    try:
        
        cur = conn.cursor()
        cur.executescript("""

        DROP TABLE IF EXISTS drzava;

        CREATE TABLE drzava (
        id INTEGER PRIMARY KEY,
        naziv text NOT NULL);
        """)
        
        print("uspjesno kreirana tablica drzava!")

        cur.execute("INSERT INTO drzava (naziv) VALUES (?)",("Hrvatska",))
        cur.execute("INSERT INTO drzava (naziv) VALUES (?)",("Austrija",))
        conn.commit()

        print("uspjesno uneseni testni podaci u tablicu drzava!")

    except Exception as e: 
        print("Dogodila se greska pri kreiranju demo podataka: ", e)
        conn.rollback()
        
    conn.close()
def procitaj_sve_podatke():
    conn = sqlite3.connect("upi_projekt.db")
    lista_drzava = []
    try:

        cur = conn.cursor()
        cur.execute(""" SELECT id, naziv FROM drzava """)

        podaci = cur.fetchall()
        
        for drza in podaci:
            # 0 - id
            # 1 - naziv

            d = Drzava(drza[0], drza[1])
            lista_drzava.append(d)

        print("uspjesno dohvaceni svi podaci iz tablice drzava!")

        for p in lista_drzava:
            print(p)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice drzava: ", e)
        conn.rollback()

    conn.close()
    return lista_drzava


def sacuvaj_novu_drzavu(naziv):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("INSERT INTO drzava (naziv) VALUES (?)", (naziv))
        conn.commit()

        print("uspjesno dodana nova drzava u bazu podataka")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju nove drzave u bazu podataka: ", e)
        conn.rollback()

    conn.close()

def izbrisi_drzavu(drzava_id):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("DELETE FROM drzava WHERE id=?;", (drzava_id))
        conn.commit()

        print("uspjesno izbrisna drzava iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri brisanju drzave iz baze podataka: ", e)
        conn.rollback()

    conn.close()

def dohvati_drzavu_po_id(drzava_id):
    conn = sqlite3.connect("upi_projekt.db")
    drzava = None
    try:

        cur = conn.cursor()
        cur.execute(" SELECT naziv FROM drzava WHERE id = ?", (drzava_id))
        podaci = cur.fetchone()

        print("podaci", podaci)
        drzava = Drzava(podaci[0], podaci[1])

        print("uspjesno dohvacena drzava iz baze podataka po ID-u")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju drzave iz baze podataka po ID-u: ", e)
        conn.rollback()

    conn.close()
    return drzava

def azuriraj_drzavu(drzava_id,naziv):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("UPDATE drzava SET naziv = ? WHERE id = ?", (naziv,drzava_id))
        conn.commit()

        print("uspjesno ažurirana drzava iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri ažuriranju drzave iz baze podataka: ", e)
        conn.rollback()

    conn.close()
