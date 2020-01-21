from bottle import Bottle, run, \
     template, debug, get, route, static_file,request,redirect,post
import os, sys
from baza import unesi_demo_podatke,sacuvaj_novog_korisnika,procitaj_sve_podatke_korisnik,dohvati_korisnika_po_id,ispisi_korisnike_po_username

#poziv funkcije koja napuni bazu test podacima
unesi_demo_podatke()
#procitaj_sve_podatke_korisnik()


#citanje svih podataka iz baze



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
    data = {"developer_name": "PMF student",
            "developer_organization": "PMF"}
    return template('index', data = data)

@app.route('/login')
def login():
    return template('login',form_akcija="/provjera_korisnickog_profila",template_lookup=[template_path])

@app.route('/provjera_korisnickog_profila',method="POST")
def provjera_korisnickog_profila():
    postdata=request.body.read()
    username=request.forms.get('user_name')
    lozinka=request.forms.get('password')
    userID=-1
    svi_korisnici=procitaj_sve_podatke_korisnik()
    for korisnik in svi_korisnici:
        if (korisnik.korisnicko_ime==username and korisnik.lozinka==lozinka):
            userID=korisnik.id
    if userID != -1:
        korisnik=dohvati_korisnika_po_id(userID)
        return template('korisnicki_profil/'+str(userID),data=korisnik,form_akcija="",template_lookup=[template_path])    
    else:
        login()
        
@app.route('/korisnicki_profil/<user_id>')
def korisnicki_profil_user(user_id):
    print("user_id", user_id)
    podaci=dohvati_korisnika_po_id(int(user_id))
    return template('korisnicki_profil',data = podaci,template_lookup=[template_path])

@app.route('/korisnicki_profil')
def korisnicki_profil():
    return template('korisnicki_profil',template_lookup=[template_path])

@app.route('/reg')
def reg():
    podaci=ispisi_korisnike_po_username()
    return template('reg', form_akcija="/dodavanje_novog_korisnika",data=podaci,template_lookup=[template_path])

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
            return user_vec_postoji ==True
    if (user_vec_postoji == False):
        sacuvaj_novog_korisnika(ime,prezime,spol,user_name,lozinka)
        svi_korisnici=procitaj_sve_podatke_korisnik()
    #else
        #poruka,pitaj profesora kako
        #kao poruka da takav korisnik vec postoji i da se ponovno unese korisnicko ime

    if(user_vec_postoji):
        return template('login',form_akcija="/provjera_korisnickog_profila",template_lookup=[template_path], user_vec_postoji = user_vec_postoji)
       
    #spremanje u bazu podataka
    print("Uspjesno spremljen korisnik!")
    for korisnik in svi_korisnici:
        if korisnik.korisnicko_ime==user_name:
            user_id=korisnik.id
    if user_id != -1:
        redirect('/korisnicki_profil/'+str(user_id))
    
run(app, host='localhost', port = 8081)
