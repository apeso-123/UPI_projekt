class Korisnik():

    def __init__(self, id, ime_prezime,spol):
        self._id = id
        self._ime_prezime = ime_prezime
        self._spol=spol

    @property
    def id(self):
        return self._id

    @property
    def ime_prezime(self):
        return self._ime_prezime

    @property
    def spol(self):
        return self._spol

    def __str__(self):
        return """
        id: {0}
        ime_prezime: {1}
        spol: {2}
        ----------------
        """.format(self._id, self.ime_prezime,self._spol)


