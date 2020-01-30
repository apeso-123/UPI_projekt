from bottle import Bottle, run, \
     template, debug, get, route, static_file,request,redirect,post
import os, sys
from baza import *
from datetime import datetime
import json
import re 

# Look if stringB is in stringA


unesi_demo_podatke()
izbrisi_poruku(9)

#Globalne varijable
sugovornik=0
id_drzave_koja_je_odabrana=0
korisnik_logiran=False
korisnik_koji_je_prijavljen=None
odabrani_grad=None
link_na_sliku=None

#Putanja
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
    return template('index',data=data,form_akcija='/pretrazivanje',template_lookup=[template_path])
@app.route('/pretrazivanje',method='POST')
def pretrazivanje():
    postdata=request.body.read()
    unos=str(request.forms.get('search')).lower()
    if unos=="":
        redirect('/')
    gradovi=procitaj_sve_podatke_grad()
    data=[]
    for g in gradovi:
        match = re.search(unos, g.naziv.lower())
        if match:
            data.append(g)
    drzave=procitaj_sve_podatke_drzava()
    for d in drzave:
        match=re.search(unos,d.naziv.lower())
        if match:
            gradovi=dohvati_gradove_koji_su_u_drzavi(d.id)
            for g in gradovi:
                data.append(g)
    return template('index',data=data,form_akcija='/pretrazivanje',template_lookup=[template_path])
@app.route('/kontakt')
def kontakt():
    return template('kontakt',template_lookup=[template_path])
@app.route('/gradovi/<ind>')
def gradovi(ind):
    index=ind
    kg=dohvati_kg_po_grad_id(index)
    lista=[]
    try:
        index=int(index)
    except Exception as e:
        if(korisnik_logiran):
            redirect('/korisnicki_profil')
        else:
            redirect('/login')

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
        lista.append(x)
        
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
                    korisnici_razgovori=ucitavanje_poruka(korisnik_koji_je_prijavljen.id)
                    return template('korisnicki_profil',data=korisnik,lista=lista,poruke=korisnici_razgovori,korisnik_logiran=korisnik_logiran,template_lookup=[template_path])

                #return template('korisnicki_profil',data=korisnik,form_akcija="",template_lookup=[template_path])
                else:
                    return template('login',form_akcija="/provjera_korisnickog_profila",korisnik_logiran=False,zastavica=True,template_lookup=[template_path])
    else:
        lista=dohvati_korisnicki_profil(korisnik_koji_je_prijavljen)
        korisnici_razgovori=ucitavanje_poruka(korisnik_koji_je_prijavljen.id)
        return template('korisnicki_profil',data=korisnik_koji_je_prijavljen,lista=lista,poruke=korisnici_razgovori,korisnik_logiran=korisnik_logiran,template_lookup=[template_path])
    if userID==-1:
        return template('login',form_akcija="/provjera_korisnickog_profila",zastavica=True,korisnik_logiran=False,template_lookup=[template_path])

def ucitavanje_poruka(korisnik):
    lista2=dohvati_korisnike_s_kojima_se_dop_prijavljeni_korisnik(korisnik)
    korisnici_razgovori=[]
    for item in lista2:   
        user=dohvati_korisnika_po_id(item)
        username=user.korisnicko_ime
        x={
            "ID_sugovornika": item,
            "USERNAME": username
        }       
        korisnici_razgovori.append(x)
    return korisnici_razgovori

@app.route('/reg')
def reg():
    podaci=ispisi_korisnike_po_username()
    return template('reg', form_akcija="/dodavanje_novog_korisnika",zastavica=False,korisnik_logiran=False,template_lookup=[template_path])

@app.route('/dodavanje_novog_korisnika',method='POST')
def dodavanje_novog_korisnika():
    postdata= request.body.read()
    svi_korisnici=procitaj_sve_podatke_korisnik()
    user_id=-1
    #Dohvacanje unesenih podataka
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
    korisnici_razgovori=ucitavanje_poruka(korisnik_koji_je_prijavljen.id)
    return template('korisnicki_profil',data=data,lista=lista,poruke=korisnici_razgovori,form_akcija="",template_lookup=[template_path])

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

    sacuvaj_novi_grad(naziv_grada,link,id_drzave_koja_je_odabrana)
    return trazi_grad_za_drzavu()

@app.route('/odjava')
def odjava():
    global korisnik_koji_je_prijavljen
    global korisnik_logiran
    korisnik_logiran=False
    korisnik_koji_je_prijavljen=None
    
    redirect('/login')
    #return template('index',data=data,template_lookup=[template_path])

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

@app.route('/poruke/<ind>')
def poruke(ind):

    sugovornik1=int(ind)
    global sugovornik
    sugovornik=sugovornik1
    user=dohvati_korisnika_po_id(sugovornik)
    username=user.korisnicko_ime
    sugovornik2=korisnik_koji_je_prijavljen.id
    poruke=dohvati_poruku_po_id_primatelja_posiljatelju(sugovornik1,sugovornik2)
    poruke.sort()
    
    return template('poruke',data=poruke,logirani=sugovornik2,username=username,form_akcija='/odgovori',template_lookup=[template_path])

@app.route('/nova_poruka')
def nova_poruka():
    index=int(request.query['korisnikid'])
    if(korisnik_logiran==True):
        if(index!=korisnik_koji_je_prijavljen.id):
            return template('nova_poruka',primatelj=index,form_akcija='/posalji_novu_poruku',odustani='/',template_lookup=[template_path])
        else:
            print("Ne mozes samom sebi slati poruku")
            redirect('/')
    else:
        return template('login',form_akcija="/provjera_korisnickog_profila",zastavica= False,korisnik_logiran=False,template_lookup=[template_path])

@app.route('/posalji_novu_poruku',method='POST')
def posalji_novu_poruku():
    postdata=request.body.read()
    broj=request.forms.get('broj')
    text=request.forms.get('textarea1')
    if(korisnik_logiran== True):
        posiljatelj=korisnik_koji_je_prijavljen.id
    else:
        login()
        posiljatelj=korisnik_koji_je_prijavljen.id

    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    sacuvaj_novu_poruku(text,posiljatelj,broj,dt_string,0)
    return poruke(broj)
@app.route('/odgovori',method='POST')
def odgovori():
    postdata=request.body.read()
    tekst=request.forms.get('tekst_poruke')
    id_posilja=korisnik_koji_je_prijavljen.id
    id_primatelja=sugovornik
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    sacuvaj_novu_poruku(tekst,id_posilja,id_primatelja,dt_string,0)

    return poruke(sugovornik)

@app.route('/azuriranje_posta')
def azuriranje_posta():
    id_posta=int(request.query['postid'])

    data=dohvati_kg_po_id(id_posta)
    return template('azuriranje_posta',data=data,form_akcija='/spremi_azurirane_podatke',template_lookup=[template_path])

@app.route('/spremi_azurirane_podatke',method='POST')
def spremi_azurirane_podatke():
    postdata=request.body.read()
    gradid=request.forms.get('gradid')
    postid=request.forms.get('postid')
    opis=request.forms.get('opis')
    znam=request.forms.get('znamenitosti')
    smjestaj=request.forms.get('smjestaj')
    prijevoz=request.forms.get('prijevoz')
    hrana=request.forms.get('hrana')
    zanimljivosti=request.forms.get('zanimljivosti')

    azuriraj_kg(postid,opis,znam,prijevoz,smjestaj,hrana,zanimljivosti,gradid,korisnik_koji_je_prijavljen.id)
    print("Spremljeni podaci!")
    redirect('/korisnicki_profil')
@app.route('/izbrisi_post')
def izbrisi_post():
    id_posta=int(request.query['postid'])
    izbrisi_kg(id_posta)
    redirect('/korisnicki_profil')

run(app, host='localhost', port = 8081)

