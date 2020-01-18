class Korisnik():
    def __init__(self, id, ime, prezime,spol, korisnicko_ime, lozinka,):
        self._id = id
        self._ime = ime
        self._prezime=prezime
        self._spol=spol
        self._korisnicko_ime=korisnicko_ime
        self._lozinka = lozinka

    @property
    def id(self):
        return self._id

    @property
    def ime(self):
        return self._ime
		
    @property
    def prezime(self):
        return self._prezime
	
    @property
    def korisnicko_ime(self):
        return self._korisnicko_ime
		
    @property
    def lozinka(self):
        return self._lozinka
		
    @property
    def spol(self):
        return self._spol

    def __str__(self):
        return """
        id: {0}
        ime: {1}
	prezime: {2}
        spol: {3}
	korisnicko_ime: {4}
	lozinka: {5}
        ----------------
        """.format(self._id, self._ime,self._prezime,self._spol,self._korisnicko_ime,self._lozinka)


