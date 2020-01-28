from bottle import Bottle, run, \
     template, debug, get, route, static_file,request,redirect,post
import os, sys
from baza import unesi_demo_podatke,sacuvaj_novog_korisnika,procitaj_sve_podatke_korisnik,azuriraj_korisnika,\
    dohvati_korisnika_po_id,ispisi_korisnike_po_username,dohvati_kg_po_korisnik_id,dohvati_grad_po_id,\
        izbrisi_drzavu,procitaj_sve_podatke_drzava,dohvati_drzavu_po_nazivu,dohvati_drzavu_po_id,\
            procitaj_sve_podatke_grad,izbrisi_grad,azuriraj_grad,dohvati_gradove_koji_su_u_drzavi, \
                sacuvaj_novi_grad,sacuvaj_novog_kg,procitaj_sve_podatke_kg,dohvati_grad_po_id,dohvati_kg_po_grad_id

import json


unesi_demo_podatke()

id_drzave_koja_je_odabrana=0
korisnik_logiran=False
korisnik_koji_je_prijavljen=None
odabrani_grad=None
link_na_sliku=None
dirname = os.path.dirname(sys.argv[0])
template_path = dirname + '\\views'
app = Bottle()
debug(True)

@app.route('/static/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root=dirname+'/static/assets/css')

@app.route('/static/<filename:re:.*\.css.map>')
def send_cssmap(filename):
    return static_file(filename, root=dirname+'/static/assets/css')

@app.route('/static/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root=dirname+'/static/assets/js')

@app.route('/static/<filename:re:.*\.js.map>')
def send_jsmap(filename):
    return static_file(filename, root=dirname+'/static/assets/js')



@app.route('/')
def index():
    data=procitaj_sve_podatke_grad()
    return template('index',data=data,template_lookup=[template_path])

@app.route('/gradovi/<ind>')
def gradovi(ind):
    index=int(ind)
    kg=dohvati_kg_po_grad_id(index)
    lista=[]

    for g in kg:
        grad=dohvati_grad_po_id(index)
        korisnik=dohvati_korisnika_po_id(g.korisnik_id)
        x={
            "id_baze": g.id_baze,
            "opis": g.opis,
            "znamenitosti": g.znamenitosti,
            "prijevoz": g.prijevoz,
            "smjestaj": g.smjestaj,
            "hrana": g.hrana,
            "zanimljivosti": g.zanimljivosti,
            "grad_id": g.grad_id,
            "korisnik_id": g.korisnik_id,
            "grad_naziv": grad.naziv,
            "korisnik_user_name": korisnik.korisnicko_ime                 
        }
        y=json.dumps(x)
        print(y)
        lista.append(x)
        korisnik_logiran=True
        korisnik_koji_je_prijavljen=korisnik

    return template('gradovi',lista=lista,template_lookup=[template_path])

@app.route('/login')
def login():
    if(korisnik_logiran!=True):
        return template('login',form_akcija="/provjera_korisnickog_profila",zastavica= False,korisnik_logiran=False,template_lookup=[template_path])
    else:
        return provjera_korisnickog_profila()


@app.route('/provjera_korisnickog_profila',method="POST")
def provjera_korisnickog_profila():
    global korisnik_logiran
    global korisnik_koji_je_prijavljen
    userID=-1
    lista=[]
    if korisnik_logiran==False:
        postdata=request.body.read()
        username=request.forms.get('user_name')
        lozinka=str(request.forms.get('password'))
        svi_korisnici=procitaj_sve_podatke_korisnik()
        for korisnik in svi_korisnici:
            print(korisnik.korisnicko_ime)
            if (korisnik.korisnicko_ime==username ):
                if (korisnik.lozinka==lozinka):
                    userID=korisnik.id
                    print("Uspješno ste se prijavili u svoj profil!"+korisnik.ime)
                    lista=dohvati_korisnicki_profil(korisnik)
                    korisnik_logiran=True
                    korisnik_koji_je_prijavljen=korisnik
                    return template('korisnicki_profil',data=korisnik,lista=lista,korisnik_logiran=korisnik_logiran,template_lookup=[template_path])

                #return template('korisnicki_profil',data=korisnik,form_akcija="",template_lookup=[template_path])
                else:
                    return template('login',form_akcija="/provjera_korisnickog_profila",korisnik_logiran=False,zastavica=True,template_lookup=[template_path])
    else:
        lista=dohvati_korisnicki_profil(korisnik_koji_je_prijavljen)
        return template('korisnicki_profil',data=korisnik_koji_je_prijavljen,lista=lista,korisnik_logiran=korisnik_logiran,template_lookup=[template_path])
    if userID==-1:
        return template('login',form_akcija="/provjera_korisnickog_profila",zastavica=True,korisnik_logiran=False,template_lookup=[template_path])

@app.route('/reg')
def reg():
    podaci=ispisi_korisnike_po_username()
    return template('reg', form_akcija="/dodavanje_novog_korisnika",zastavica=False,korisnik_logiran=False,template_lookup=[template_path])

@app.route('/dodavanje_novog_korisnika',method='POST')
def dodavanje_novog_korisnika():
    postdata= request.body.read()
    svi_korisnici=procitaj_sve_podatke_korisnik()
    user_id=-1
    #dohvacamo podatke po atributu "txt_reg_ime" definiranog u input elementu forme
    ime=request.forms.get('txt_reg_ime')
    prezime=request.forms.get('txt_reg_prezime')
    spol=request.forms.get('reg_spol')
    user_name=request.forms.get('txt_reg_user')
    lozinka=request.forms.get('reg_lozinka')
    
    user_vec_postoji= False
    
    for korisnik in svi_korisnici:
        user_id=korisnik.id
        if korisnik.korisnicko_ime==user_name:
            user_vec_postoji= True
        
    if (user_vec_postoji == False):
        sacuvaj_novog_korisnika(ime,prezime,spol,user_name,lozinka)
        print("Novi korisnik uspješno spremljen!")
        svi_korisnici=procitaj_sve_podatke_korisnik()
    else:
        print("Ponovite upis!")
        return template('reg',form_akcija="/dodavanje_novog_korisnika",zastavica=True,korisnik_logiran=False,template_lookup=[template_path])
        
    for korisnik in svi_korisnici:
        if korisnik.korisnicko_ime==user_name:
            dohvati_korisnicki_profil(korisnik)      

  
@app.route('/korisnicki_profil')
def korisnicki_profil():
    data=korisnik_koji_je_prijavljen
    lista=dohvati_korisnicki_profil(data)

    return template('korisnicki_profil',data=data,lista=lista,form_akcija="",template_lookup=[template_path])

def dohvati_korisnicki_profil(korisnik):
    global korisnik_logiran
    global korisnik_koji_je_prijavljen
    korisnik_grad=dohvati_kg_po_korisnik_id(korisnik.id)
    print("U metodi dohvati korisnicki profil")
    lista=[]

    for g in korisnik_grad:
        grad=dohvati_grad_po_id(g.grad_id)
        x={
            "id_baze": g.id_baze,
            "opis": g.opis,
            "znamenitosti": g.znamenitosti,
            "prijevoz": g.prijevoz,
            "smjestaj": g.smjestaj,
            "hrana": g.hrana,
            "zanimljivosti": g.zanimljivosti,
            "grad_id": g.grad_id,
            "korisnik_id": g.korisnik_id,
            "grad_naziv": grad.naziv,
            "korisnik_user_name":korisnik.korisnicko_ime                 
        }
        y=json.dumps(x)
        print(y)
        lista.append(x)
        korisnik_logiran=True
        korisnik_koji_je_prijavljen=korisnik
    return lista

@app.route('/odabiranje_drzave')
def odabiranje_drzave():
    podaci=procitaj_sve_podatke_drzava()
    return template('odabiranje_drzave',data=podaci,form_akcija="trazi_grad_za_drzavu",template_lookup=[template_path])

@app.route('/trazi_grad_za_drzavu',method='POST')
def trazi_grad_za_drzavu():
    global id_drzave_koja_je_odabrana
    postdata= request.body.read()
    drzava=request.forms.get('selectbasic')
    if(drzava==None):
        drzava=dohvati_drzavu_po_id(id_drzave_koja_je_odabrana)
    else:
        id_drzave_koja_je_odabrana=int(drzava)
    grad=dohvati_gradove_koji_su_u_drzavi(id_drzave_koja_je_odabrana)
    return template('odaberi_grad',grad=grad,drzava_id=id_drzave_koja_je_odabrana,form_akcija="/dodavanje_obiljezja_grada",template_lookup=[template_path])

@app.route('/odaberi_grad',method='POST')
def odaberi_grad():
    return template('odaberi_grad',form_akcija="/dodavanje_obiljezja_grada",template_lookup=[template_path])

@app.route('/dodavanje_obiljezja_grada',method='POST')
def dodavanje_obiljezja_grada():
    global odabrani_grad
    global link_na_sliku
    postdata=request.body.read()
    grad=request.forms.get('odabrani_grad')
    odabrani_grad=grad
    link_na_sliku=dohvati_grad_po_id(grad).link_slike
    return template('dodavanje_obiljezja_grada',grad=grad,link_slike=link_na_sliku,form_akcija="/spremanje_obiljezja_grada",template_lookup=[template_path])

@app.route('/spremanje_obiljezja_grada',method='POST')
def spremanje_obiljezja_grada():
    postdata=request.body.read()
    grad_id=odabrani_grad
    link_slike=request.forms.get('link_slike')
    opis=request.forms.get('opis')
    znam=request.forms.get('znamenitosti')
    smjestaj=request.forms.get('smjestaj')
    prijevoz=request.forms.get('prijevoz')
    hrana=request.forms.get('hrana')
    zanimljivosti=request.forms.get('zanimljivosti')
    print(grad_id)
    sacuvaj_novog_kg(opis,znam,prijevoz,smjestaj,hrana,zanimljivosti,grad_id,korisnik_koji_je_prijavljen.id)
    
    return korisnicki_profil()
    
@app.route('/dodaj_novi_grad')
def dodaj_novi_grad():
    return template('dodaj_novi_grad',form_akcija="spremanje_novog_grada",template_lookup=[template_path])

@app.route('/spremanje_novog_grada',method='POST')
def spremanje_novog_grada():
    postdata=request.body.read()
    naziv_grada=request.forms.get('naziv_novog_grada')
    link=request.forms.get('link_na_sliku')
    print("Tijekom SPremsnjs",id_drzave_koja_je_odabrana)
    sacuvaj_novi_grad(naziv_grada,link,id_drzave_koja_je_odabrana)
    return trazi_grad_za_drzavu()

@app.route('/odjava')
def odjava():
    global korisnik_koji_je_prijavljen
    global korisnik_logiran
    korisnik_logiran=False
    korisnik_koji_je_prijavljen=None
    data=procitaj_sve_podatke_grad()
    return template('index',data=data,template_lookup=[template_path])

@app.route('/postavke_profila')
def postavke_profila():
    podaci=korisnik_koji_je_prijavljen
    return template('postavke_profila',data=podaci,form_akcija='/spremi_promjene',template_lookup=[template_path])

@app.route('/spremi_promjene',method='POST')
def spremi_promjene():
    postdata=request.body.read()
    ime=request.forms.get('txt_reg_ime')
    prezime=request.forms.get('txt_reg_prezime')
    spol=request.forms.get('reg_spol')
    lozinka=request.forms.get('reg_lozinka')
    azuriraj_korisnika(korisnik_koji_je_prijavljen.id,ime,prezime,spol,lozinka)
    return korisnicki_profil()

run(app, host='localhost', port = 8081)

