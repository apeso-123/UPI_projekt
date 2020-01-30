import sqlite3
import os, sys
from datetime import datetime


dirname = os.path.dirname(sys.argv[0])
sys.path.append(dirname.replace('\\', '/') + '/Entiteti/')

from drzava import Drzava
from grad import Grad
from korisnik import Korisnik
from korisnik_grad import Korisnik_Grad
from poruka import Poruka

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

        CREATE TABLE IF NOT EXISTS korisnik_grad (
        id_baze INTEGER PRIMARY KEY,
        opis text NOT NULL,
        znamenitosti text NOT NULL,
        prijevoz text NOT NULL,
        smjestaj text NOT NULL,
        hrana text NOT NULL,
        zanimljivosti text NOT NULL,
        grad_id INTEGER NOT NULL,
        korisnik_id INTEGER NOT NULL,
        FOREIGN KEY (grad_id) REFERENCES grad (id_grad),
        FOREIGN KEY (korisnik_id) REFERENCES korisnik (id_korisnik)
        );

        CREATE TABLE IF NOT EXISTS poruka (
        id_poruka INTEGER PRIMARY KEY,
        tekst text NOT NULL,
        id_posiljatelj INTEGER NOT NULL,
        id_primatelj INTEGER NOT NULL,
        datum text NOT NULL,
        procitana INTEGER NOT NULL,
        FOREIGN KEY (id_posiljatelj) REFERENCES korisnik (id_korisnik),
        FOREIGN KEY (id_primatelj) REFERENCES korisnik (id_korisnik)
        )
        """)

        conn.commit()

        print("uspjesno uneseni testni podaci!")

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
        cur.execute(""" SELECT id, naziv FROM drzava """)        
        podaci = cur.fetchall()        
        for drza in podaci:
            # 0 - id
            # 1 - naziv
            d = Drzava(drza[0], drza[1])
            lista_drzava.append(d)

        print("uspjesno dohvaceni svi podaci iz tablice drzava!")


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
def dohvati_drzavu_po_nazivu(naziv):
    conn =sqlite3.connect("upi_projekt.db")
    drzava = None
    try:
        cur =conn.cursor()
        cur.execute(" SELECT id,naziv FROM drzava WHERE naziv = ?", ([naziv]))
        podaci = cur.fetchone()

        print("podaci", podaci)
        drzava = Drzava(podaci[0], podaci[1])

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju drzave po nazivu iz baze podataka: ", e)
        conn.rollback()

    conn.close()
    return drzava

def izbrisi_drzavu(drzava_id):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("DELETE FROM drzava WHERE id=?;", (str(drzava_id)))
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
        cur.execute(" SELECT id,naziv FROM drzava WHERE id= ?", ([str(drzava_id)]))
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
        cur.execute("INSERT INTO grad (naziv,link_slike,id_drzava) VALUES (?,?,?)", (naziv,link_slike,str(id_drzava)))
        conn.commit()

        print("uspjesno dodana novi grad u bazu podataka")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju novog grada u bazu podataka: ", e)
        conn.rollback()

    conn.close()

def izbrisi_grad(grad_id_):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("DELETE FROM grad WHERE id_grad=?;", (str(grad_id_)))
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
        cur.execute(" SELECT id_grad,naziv,link_slike,id_drzava FROM grad WHERE id_grad= ?", ([str(grad_id)]))
        podaci = cur.fetchone()

        print("podaci", podaci)
        grad = Grad(podaci[0], podaci[1],podaci[2],podaci[3])

        print("uspjesno dohvacen grad iz baze podataka po ID-u")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju grada iz baze podataka po ID-u: ", e)
        conn.rollback()

    conn.close()
    return grad

def dohvati_gradove_koji_su_u_drzavi(drzava_id):
    conn = sqlite3.connect("upi_projekt.db")
    lista_gradova = []
    try:
        cur = conn.cursor()
        cur.execute(""" SELECT id_grad, naziv, link_slike, id_drzava FROM grad WHERE id_drzava= ? """,([str(drzava_id)]))        
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

def azuriraj_grad(grad_id,naziv,link,drzava_id):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("UPDATE grad SET naziv = ?, link_slike = ? ,id_drzava = ? WHERE id_grad = ?", (naziv,link,[str(drzava_id)],[str(grad_id)]))
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

def ispisi_korisnike_po_username():
    con = sqlite3.connect("upi_projekt.db")
    lista=[]
    try:
        cur =con.cursor()
        cur.execute(""" SELECT korisnicko_ime  FROM korisnik """)
        podaci=cur.fetchall()
        for user in podaci:
            lista.append(user)
    except Exception as e:
        print("Pogreška prilikom dohvaćanja svih korisničkih imena iz baze podataka",e)
        conn.rollback()
    con.close()
    return lista

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
        cur.execute("DELETE FROM korisnik WHERE id_korisnik=?;", ([str(id_)]))
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
        cur.execute(" SELECT id_korisnik, ime, prezime,spol,korisnicko_ime,lozinka FROM korisnik WHERE id_korisnik = ?", ([str(id_)]))
        podaci = cur.fetchone()

        print("podaci", podaci)
        korisnik = Korisnik(podaci[0], podaci[1],podaci[2],podaci[3],podaci[4],podaci[5])

        print("uspjesno dohvacena korisnik iz baze podataka po ID-u")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju korisnika iz baze podataka po ID-u: ", e)
        conn.rollback()

    conn.close()
    return korisnik

def azuriraj_korisnika(id_korisnika,ime,prezime,spol,lozinka):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("UPDATE korisnik SET ime = ?, prezime = ?, spol = ?, lozinka = ? WHERE id_korisnik = ?", (ime,prezime,spol,lozinka,str(id_korisnika)))
        conn.commit()

        print("uspjesno ažuriran korisnik iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri ažuriranju korisnika iz baze podataka: ", e)
        conn.rollback()

    conn.close()

############# tablica KORISNIK_GRAD ######################    
def procitaj_sve_podatke_kg():
    conn = sqlite3.connect("upi_projekt.db")
    lista_kg = []
    try:
        cur = conn.cursor()
        cur.execute(""" SELECT id_baze,opis,znamenitosti,prijevoz,smjestaj,hrana,zanimljivosti,grad_id,korisnik_id FROM korisnik_grad """)        
        podaci = cur.fetchall()        
        for k in podaci:
            # 0 - id
            # 1 - naziv
            d = Korisnik_Grad(k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7], k[8])
            lista_kg.append(d)

        print("uspjesno dohvaceni svi podaci iz tablice korisnik_grad!")

        for p in lista_kg:
            print(p)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice drzava: ", e)
        conn.rollback()

    conn.close()
    return lista_kg
     
def sacuvaj_novog_kg(opis,znamenitosti,prijevoz,smjestaj,hrana,zanimljivosti,grad_id,korisnik_id):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("INSERT INTO korisnik_grad (opis,znamenitosti,prijevoz,smjestaj,hrana,zanimljivosti,grad_id,korisnik_id) VALUES(?,?,?,?,?,?,?,?)",(opis,znamenitosti,prijevoz,smjestaj,hrana,zanimljivosti,grad_id,korisnik_id))        
        conn.commit()

        print("uspjesno dodan novi korisnik_grad u bazu podataka")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju novog korisnik_grada u bazu podataka: ", e)
        conn.rollback()

    conn.close()

def izbrisi_kg(kg_id):
    conn = sqlite3.connect("upi_projekt.db")
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM korisnik_grad WHERE id_baze=?;", ([str(kg_id)]))
        conn.commit()

        print("uspjesno izbrisan korisnik_grad iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri brisanju korisnik_grada iz baze podataka: ", e)
        conn.rollback()

    conn.close()

def dohvati_kg_po_id(kg):
    conn = sqlite3.connect("upi_projekt.db")
    podatak = None
    try:

        cur = conn.cursor()
        cur.execute(" SELECT * FROM korisnik_grad WHERE id_baze = ?", (str(kg)))
        k = cur.fetchone()

        print("podaci", k)
        podatak= Korisnik_Grad(k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7], k[8])

        print("uspjesno dohvacen korisnik_grad iz baze podataka po ID-u")

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju drzave iz baze podataka po ID-u: ", e)
        conn.rollback()

    conn.close()
    return podatak

def azuriraj_kg(id_baze,opis,znamenitosti,prijevoz,smjestaj,hrana,zanimljivosti,grad_id,korisnik_id):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("UPDATE korisnik_grad SET opis = ?,znamenitosti = ?, prijevoz = ?, smjestaj = ?, hrana = ?,zanimljivosti = ?,grad_id = ?,korisnik_id = ?  WHERE id_baze = ?", (opis,znamenitosti,prijevoz,smjestaj,hrana,zanimljivosti,grad_id,korisnik_id,id_baze))
        conn.commit()

        print("uspjesno ažuriran korisnik_grad iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri ažuriranju drzave iz baze podataka: ", e)
        conn.rollback()

    conn.close()

def dohvati_kg_po_korisnik_id(ki):
    conn = sqlite3.connect("upi_projekt.db")
    lista_kg = []
    try:
        cur = conn.cursor()
        cur.execute(" SELECT id_baze,opis,znamenitosti,prijevoz,smjestaj,hrana,zanimljivosti,grad_id,korisnik_id FROM korisnik_grad WHERE korisnik_id = ?", ([str(ki)]))        
        podaci = cur.fetchall()        
        for k in podaci:
            d = Korisnik_Grad(k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7], k[8])
            lista_kg.append(d)

        print("uspjesno dohvaceni svi podaci iz tablice korisnik_grad!")

        for p in lista_kg:
            print(p)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice korisnik_grad: ", e)
        conn.rollback()

    conn.close()
    return lista_kg

def dohvati_kg_po_grad_id(ki):
    conn = sqlite3.connect("upi_projekt.db")
    lista_kg = []
    try:
        cur = conn.cursor()
        cur.execute(" SELECT id_baze,opis,znamenitosti,prijevoz,smjestaj,hrana,zanimljivosti,grad_id,korisnik_id FROM korisnik_grad WHERE grad_id = ?", ([str(ki)]))        
        podaci = cur.fetchall()        
        for k in podaci:
            d = Korisnik_Grad(k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7], k[8])
            lista_kg.append(d)

        print("uspjesno dohvaceni svi podaci iz tablice korisnik_grad!")

        for p in lista_kg:
            print(p)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice korisnik_grad: ", e)
        conn.rollback()

    conn.close()
    return lista_kg

############### tablica PORUKE ###########################

def procitaj_sve_podatke_poruka():
    conn = sqlite3.connect("upi_projekt.db")
    lista_poruka = []
    try:
        cur = conn.cursor()
        cur.execute(""" SELECT id_poruka,tekst,id_posiljatelj,id_primatelj,datum,procitana FROM poruka """)        
        podaci = cur.fetchall()        
        for p in podaci:
            # 0 - id
            # 1 - naziv
            d = Poruka(p[0], p[1],p[2],p[3],p[4],p[5])
            print(d)
            lista_poruka.append(d)

        print("uspjesno dohvaceni svi podaci iz tablice poruka!")


    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice poruka: ", e)
        conn.rollback()

    conn.close()
    return lista_poruka
    
def sacuvaj_novu_poruku(tekst,pos,prim,datum,procitana):
    conn = sqlite3.connect("upi_projekt.db")
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO poruka (tekst,id_posiljatelj,id_primatelj,datum,procitana) VALUES (?,?,?,?,?)", (tekst,pos,prim,datum,str(procitana)))
        conn.commit()

        print("uspjesno dodana nova poruka u bazu podataka")

    except Exception as e: 
        print("Dogodila se greska pri dodavanju nove poruke u bazu podataka: ", e)
        conn.rollback()

    conn.close()
def dohvati_poruku_po_id_primatelja_posiljatelju(primatelj,posiljatelj):
    conn =sqlite3.connect("upi_projekt.db")
    poruke = []
    try:
        cur = conn.cursor()
        cur.execute(" SELECT id_poruka,tekst,id_posiljatelj,id_primatelj,datum,procitana FROM poruka WHERE id_posiljatelj = ? AND id_primatelj = ?", (str(posiljatelj),str(primatelj)))        
        podaci = cur.fetchall()    
            
        for k in podaci:
            d = Poruka(k[0], k[1], k[2], k[3], k[4], k[5])
            poruke.append(d)

        print("uspjesno dohvaceni svi podaci iz tablice poruka!")

        for p in poruke:
            print(p)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju po id u prim i posilj svih podataka iz tablice poruka: ", e)
        conn.rollback()
    try:
        cur = conn.cursor()
        cur.execute(" SELECT id_poruka,tekst,id_posiljatelj,id_primatelj,datum,procitana FROM poruka WHERE id_posiljatelj = ? AND id_primatelj = ?", (str(primatelj),str(posiljatelj)))        
        podaci = cur.fetchall()        
        for k in podaci:
            d = Poruka(k[0], k[1], k[2], k[3], k[4], k[5])
            poruke.append(d)

        print("uspjesno dohvaceni svi podaci iz tablice poruka!")

        for p in poruke:
            print(p)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice poruka: ", e)
        conn.rollback()

    conn.close()
    return poruke


def izbrisi_poruku(poruka_id):
    conn = sqlite3.connect("upi_projekt.db")
    try:

        cur = conn.cursor()
        cur.execute("DELETE FROM poruka WHERE id_poruka=?;", ([str(poruka_id)]))
        conn.commit()

        print("uspjesno izbrisna poruka iz baze podataka")

    except Exception as e: 
        print("Dogodila se greska pri brisanju poruke iz baze podataka: ", e)
        conn.rollback()

    conn.close()

def dohvati_poruku_po_id(poruka_id):
    conn =sqlite3.connect("upi_projekt.db")
    poruke = []
    try:
        cur = conn.cursor()
        cur.execute(" SELECT id_poruka,tekst,id_posiljatelj,id_primatelj,datum,procitana FROM poruka WHERE id_poruka = ?", ([str(poruka_id)]))        
        podaci = cur.fetchall()        
        for k in podaci:
            d = Poruka(k[0], k[1], k[2], k[3], k[4], k[5])
            poruke.append(d)

        print("uspjesno dohvaceni svi podaci iz tablice poruka!")

        for p in poruke:
            print(p)

    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice poruka: ", e)
        conn.rollback()

    conn.close()
    return poruke

def dohvati_korisnike_s_kojima_se_dop_prijavljeni_korisnik(id_korisnik):
    conn =sqlite3.connect("upi_projekt.db")
    lista_korisnika_s_kojima_razgovara=[]
    try:
        cur = conn.cursor()
        cur.execute(" SELECT id_poruka,tekst,id_posiljatelj,id_primatelj,datum,procitana FROM poruka WHERE id_posiljatelj = ?",([str(id_korisnik)]))        
        podaci = cur.fetchall()        
        for k in podaci:
            d = Poruka(k[0], k[1], k[2], k[3], k[4], k[5])
            if(d.id_primatelj not in lista_korisnika_s_kojima_razgovara):
                lista_korisnika_s_kojima_razgovara.append(d.id_primatelj)
        
        print("uspjesno dohvaceni svi podaci iz tablice poruka!")
    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice poruka: ", e)
        conn.rollback()
    try:
        cur = conn.cursor()
        cur.execute(" SELECT id_poruka,tekst,id_posiljatelj,id_primatelj,datum,procitana FROM poruka WHERE id_primatelj = ?",([str(id_korisnik)]))        
        podaci = cur.fetchall()        
        for k in podaci:
            d = Poruka(k[0], k[1], k[2], k[3], k[4], k[5])
            if(d.id_posiljatelj not in lista_korisnika_s_kojima_razgovara):
                lista_korisnika_s_kojima_razgovara.append(d.id_posiljatelj)
        
        print("uspjesno dohvaceni svi podaci iz tablice poruka!")
    except Exception as e: 
        print("Dogodila se greska pri dohvacanju svih podataka iz tablice poruka: ", e)
        conn.rollback()

    conn.close()
    return lista_korisnika_s_kojima_razgovara

