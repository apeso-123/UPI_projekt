class Poruka():
    def __init__(self, id,tekst,id_posiljatelj,id_primatelj,datum,procitana):
        self._id = id
        self._tekst= tekst
        self._id_posiljatelj=id_posiljatelj
        self._id_primatelj=id_primatelj
        self._datum=datum
        self._procitana=procitana
        

    @property
    def id(self):
        return self._id

    @property
    def tekst(self):
        return self._tekst
    
    @property
    def id_posiljatelj(self):
        return self._id_posiljatelj

    @property
    def id_primatelj(self):
        return self._id_primatelj

    @property
    def datum(self):
        return self._datum

    @property
    def procitana(self):
        return self._procitana

    def __str__(self):
        return """
        id: {0}
        tekst: {1}
        id_posiljate: {2}
        id_primatelj: {3}
        datum: {4}
        procitana: {5}
        ----------------
        """.format(self._id, self._tekst,self._id_posiljatelj,self._id_primatelj,self._datum,self._procitana)
    
    def __lt__(self,other):
        return self._id.__lt__(other._id)
    def __le__(self,other):
        return self._id.__le__(other._id)


