class Korisnik_Grad():
    def __init__(self, id_baze,opis,znamenitosti,prijevoz,smjestaj,hrana,zanimljivosti,grad_id,korisnik_id):
        self._id = id_baze
        self._korisnik_id=korisnik_id
        self._grad_id=grad_id
        self._opis=opis
        self._znamenitosti=znamenitosti
        self._prijevoz=prijevoz
        self._smjestaj=smjestaj
        self._hrana=hrana
        self._zanimljivosti=zanimljivosti

    @property
    def id_baze(self):
        return self._id

    @property
    def korisnik_id(self):
        return self._korisnik_id

    @property
    def grad_id(self):
        return self._grad_id

    @property
    def opis(self):
        return self._opis

    @property
    def znamenitosti(self):
        return self._znamenitosti

    @property
    def prijevoz(self):
        return self._prijevoz

    @property
    def smjestaj(self):
        return self._smjestaj

    @property
    def hrana(self):
        return self._hrana

    @property
    def zanimljivosti(self):
        return self._zanimljivosti
    
    def __str__(self):
        return """
        id: {0}
        id_korisnika: {1}
        id_grad: {2}
        opis: {3}
        znamenitosti: {4}
        prijevoz: {5}
        smjestaj: {6}
        hrana: {7}
        zanimljivosti: {8}
        ----------------
        """.format(self._id, self._korisnik_id,self._grad_id,self._opis,self._znamenitosti,self._prijevoz,self._smjestaj,self._hrana,self._zanimljivosti)


