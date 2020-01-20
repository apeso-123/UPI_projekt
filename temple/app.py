from bottle import Bottle, run, \
     template, debug, get, route, static_file,request,redirect,post
import os, sys
from baza import unesi_demo_podatke,sacuvaj_novog_korisnika,procitaj_sve_podatke_korisnik

#poziv funkcije koja napuni bazu test podacima
unesi_demo_podatke()
procitaj_sve_podatke_korisnik()


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
    
    
@app.route('/korisnicki_profil/<user_id>')
def korisnicki_profil(user_id):
    podaci=dohvati_korisnika_po_id(user_id)
    return template('korisnicki_profil',data=podaci,template.lookup=[template_path]
    

@app.route('/reg')
def reg():
    return template('reg', form_akcija="/dodavanje_novog_korisnika",template_lookup=[template_path])

@app.route('/dodavanje_novog_korisnika',method='POST')
def dodavanje_novog_korisnika():
    postdata= request.body.read()
    svi_korisnici=procitaj_sve_podatke_korisnik()
    
    #dohvacamo podatke po atributu "txt_reg_ime" definiranog u input elementu forme
    ime=request.forms.get('txt_reg_ime')
    prezime=request.forms.get('txt_reg_prezime')
    spol=request.forms.get('reg_spol')
    user_name=request.forms.get('txt_reg_user')
    lozinka=request.forms.get('reg_lozinka')

    for korisnik in svi_korisnici:
        if korisnik.korisnicko_ime==user_name:
            return 
                    
    #spremanje u bazu podataka
    sacuvaj_novog_korisnika(ime,prezime,spol,user_name,lozinka)
    print("Uspjesno spremljen korisnik!")
    print(ime)
    redirect('/login')
    
run(app, host='localhost', port = 8081)
