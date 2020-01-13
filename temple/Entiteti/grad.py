class Grad():

    def __init__(self, id, naziv,link_slike):
        self._id = id
        self._naziv = naziv
        self._link_slike=link_slike

    @property
    def id(self):
        return self._id

    @property
    def naziv(self):
        return self._naziv

    @property
    def link_slike(self):
        return self._link_slike

    def __str__(self):
        return """
        id: {0}
        naziv: {1}
        link_na_sliku: {2}
        ----------------
        """.format(self._id, self._naziv,self._link_slike)


