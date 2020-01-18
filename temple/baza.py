import sqlite3
import os, sys

dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/Entiteti/')

from drzava import Drzava
from grad import Grad
from korisnik import Korisnik

def unesi_demo_podatke():
    conn = sqlite3.connect("upi_projekt.db")

    try:
        
        cur = conn.cursor()
        cur.executescript("""
       
        CREATE TABLE IF NOT EXISTS drzava (
        id INTEGER PRIMARY KEY,
        naziv text NOT NULL);

        
        
        CREATE TABLE IF NOT EXISTS grad (
        id_grad INTEGER PRIMARY KEY,
        naziv text NOT NULL,
        link_slike text NOT NULL,
        id_drzava INTEGER NOT NULL,
        FOREIGN KEY (id_drzava) REFERENCES drzava (id)
        );

        

        CREATE TABLE IF NOT EXISTS korisnik (
        id_korisnik INTEGER PRIMARY KEY,
        ime text NOT NULL,
        prezime text NOT NULL,
        spol text NOT NULL,
        korisnicko_ime text NOT NULL,
        lozinka text NOT NULL
        );
        
        """)
        
        print("uspjesno kreirana tablica drzava i grad!")

        #cur.execute("INSERT INTO drzava (naziv) VALUES (?)",("Hrvatska",))
        #cur.execute("INSERT INTO drzava (naziv) VALUES (?)",("Austrija",))
        #cur.execute("INSERT INTO grad (naziv,link_slike,id_drzava) VALUES (?,?,?)",("Zagreb","https://slikezadesktop.com/wp-content/uploads/2019/01/katedrala-zagreb-slike-za-pozadine-564x376.jpg",1,))
        #cur.execute("INSERT INTO grad (naziv,link_slike,id_drzava) VALUES (?,?,?)",("Beč","http://www.pogled.ba/storage/cache/images/d/9/d/5/SMR6uC0i_bec_bozic_1_1_475_316_85_s_c1.jpg",2,))
        #cur.execute("INSERT INTO korisnik (ime,prezime,spol,korisnicko_ime,lozinka) VALUES (?,?,?,?,?)",("Antonia","Peso","Ž","apeso","12345678",))
        conn.commit()

        print("uspjesno uneseni testni podaci u tablicu drzava i grad!")

    except Exception as e: 
        print("Dogodila se greska pri kreiranju demo podataka: ", e)
        conn.rollback()
        
    conn.close()
############# tablica DRŽAVA ######################    
def procitaj_sve_podatke_drzava():
    conn = sqlite3.connect("upi_projekt.db")
    lista_drzava = []
    try:
        cur = conn.cursor()
        cur.execute(""" SELECT id_drzava, naziv FROM drzava """)        
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
        cur.execute("DELETE FROM drzava WHERE id_drzava=?;", (str(drzava_id)))
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
        cur.execute(" SELECT naziv FROM drzava WHERE id_drzava = ?", (str(drzava_id)))
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
        cur.execute("UPDATE drzava SET naziv = ? WHERE id_drzava = ?", (naziv,str(drzava_id)))
        conn.commit()

        print("uspjesno ažurirana drzava iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri ažuriranju drzave iz baze podataka: ", e)
        conn.rollback()

    conn.close()
    
################## tablica GRAD ####################
def procitaj_sve_podatke_grad():
    conn = sqlite3.connect("upi_projekt.db")
    lista_gradova = []
    try:
        cur = conn.cursor()
        cur.execute(""" SELECT id_grad, naziv, link_slike, id_drzava FROM grad """)        
        podaci = cur.fetchall()        
        for grad in podaci:
            # 0 - id
            # 1 - naziv
            # 2 - link_slike
            # 3 - id_drzava
            g = Grad(grad[0], grad[1], grad[2], grad[3])
            lista_gradova.append(g)

        print("uspjesno dohvaceni svi podaci iz tablice drzava!")

        for g in lista_gradova:
            print(g)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice drzava: ", e)
        conn.rollback()

    conn.close()
    return lista_gradova


def sacuvaj_novi_grad(naziv,link_slike,id_drzava):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("INSERT INTO grad (naziv,link_slike,id_drzava) VALUES (?,?,?)", (naziv,link_slike,id_drzava))
        conn.commit()

        print("uspjesno dodana novi grad u bazu podataka")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju novog grada u bazu podataka: ", e)
        conn.rollback()

    conn.close()

def izbrisi_grad(grad_id):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("DELETE FROM grad WHERE id_grad=?;", (str(grad_id)))
        conn.commit()

        print("uspjesno izbrisan grad iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri brisanju grada iz baze podataka: ", e)
        conn.rollback()

    conn.close()

def dohvati_grad_po_id(grad_id):
    conn = sqlite3.connect("upi_projekt.db")
    grad = None
    try:

        cur = conn.cursor()
        cur.execute(" SELECT naziv,link_slike,id_drzava FROM grad WHERE id_grad= ?", (str(grad_id)))
        podaci = cur.fetchone()

        print("podaci", podaci)
        grad = Grad(podaci[0], podaci[1],podaci[2],podaci[3])

        print("uspjesno dohvacen grad iz baze podataka po ID-u")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju grada iz baze podataka po ID-u: ", e)
        conn.rollback()

    conn.close()
    return grad

def azuriraj_grad(grad_id,naziv,link,drzava_id):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("UPDATE grad SET naziv = ?, link_slike = ? ,id_drzava = ? WHERE id_grad = ?", (naziv,link,str(drzava_id),str(grad_id)))
        conn.commit()

        print("uspjesno ažuriran grad iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri ažuriranju grada iz baze podataka: ", e)
        conn.rollback()

    conn.close()

################### tablica KORISNIK ##############################

def procitaj_sve_podatke_korisnik():
    conn = sqlite3.connect("upi_projekt.db")
    lista_korisnika = []
    try:
        cur = conn.cursor()
        cur.execute(""" SELECT id_korisnik,ime,prezime,spol,korisnicko_ime,lozinka FROM korisnik """)        
        podaci = cur.fetchall()        
        for k in podaci:
            # 0 - id
            # 1 - ime
            # 2 - prezime
            # 3 - spol
            # 4 - korisnicko_ime
            # 5 - lozinka
            d = Korisnik(k[0], k[1],k[2],k[3],k[4],k[5])
            lista_korisnika.append(d)

        print("uspjesno dohvaceni svi podaci iz tablice korisnik!")

        for p in lista_korisnika:
            print(p)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice korisnik: ", e)
        conn.rollback()

    conn.close()
    return lista_korisnika


def sacuvaj_novog_korisnika(ime,prezime,spol,korisnicko_ime,loz):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("INSERT INTO korisnik (ime,prezime,spol,korisnicko_ime,lozinka) VALUES (?,?,?,?,?)", (ime,prezime,spol,korisnicko_ime,loz))
        conn.commit()

        print("uspjesno dodan novi korisnik u bazu podataka")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju novog korisnika u bazu podataka: ", e)
        conn.rollback()

    conn.close()

def izbrisi_korisnika(id_):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("DELETE FROM korisnik WHERE id_korisnik=?;", (str(id_)))
        conn.commit()

        print("uspjesno izbrisan korisnik iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri brisanju korisnika iz baze podataka: ", e)
        conn.rollback()

    conn.close()

def dohvati_korisnika_po_id(id_):
    conn = sqlite3.connect("upi_projekt.db")
    korisnik = None
    try:

        cur = conn.cursor()
        cur.execute(" SELECT ime,prezime,spol,korisnicko_ime,lozinka FROM korisnik WHERE id_korisnik = ?", (str(id_)))
        podaci = cur.fetchone()

        print("podaci", podaci)
        korisnik = Korisnik(podaci[0], podaci[1],podaci[2],podaci[3],podaci[4],podaci[5])

        print("uspjesno dohvacena korisnik iz baze podataka po ID-u")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju korisnika iz baze podataka po ID-u: ", e)
        conn.rollback()

    conn.close()
    return korisnik

def azuriraj_korisnika(id_korisnika,ime,prezime,spol,korisnicko_ime,lozinka):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("UPDATE korisnik SET ime = ?, prezime = ?, spol = ?, korisnicko_ime = ?, lozinka = ? WHERE id_korisnik = ?", (ime,prezime,spol,korisnicko_ime,str(lozinka),str(id_korisnika)))
        conn.commit()

        print("uspjesno ažuriran korisnik iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri ažuriranju korisnika iz baze podataka: ", e)
        conn.rollback()

    conn.close()

