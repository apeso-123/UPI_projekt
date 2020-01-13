from bottle import Bottle, run, \
     template, debug, get, route, static_file
import os, sys
from baza import unesi_demo_podatke, procitaj_sve_podatke, dohvati_drzavu_po_id


#poziv funkcije koja napuni bazu test podacima
unesi_demo_podatke()

#citanje svih podataka iz baze
procitaj_sve_podatke()


dirname = os.path.dirname(sys.argv[0])
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
    return template('login')


@app.route('/reg')
def reg():
    return template('reg')
run(app, host='localhost', port = 8081)
