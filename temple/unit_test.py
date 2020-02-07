import sys
import os
import unittest
from itertools import permutations
from baza import *
if __name__=='__main__':
    sys.path.append(os.path.abspath(".."))
from Entiteti.poruka import Poruka

class TestTrokut(unittest.TestCase):      
    def setUp(self):
        unesi_demo_podatke()
    def tearDown(self):
        os.remove("upi_projekt.db")
    def test_init_type_error_string_arg(self):
        with self.assertRaises(TypeError):
            Poruka(1,"Hello","r",3,0)
    def test_init_type_error_string_arg_2(self):
        with self.assertRaises(TypeError):
            Poruka(1,"Hello",3,"r",0)
    def test_init_type_error_string_arg_3(self):
        with self.assertRaises(TypeError):
            Poruka(1,"Hello",2,3,0)

    def test_select_drzava_po_nazivu_ispravno(self):
        sacuvaj_novu_drzavu('Indija')
        self.assertCountEqual([dohvati_drzavu_po_nazivu('Indija').naziv],['Indija']) 

    def test_select_drzava_po_nazivu_krivo(self):
        sacuvaj_novu_drzavu("Indija")
        self.assertIsNone(dohvati_drzavu_po_nazivu('ime'))   
        
    def test_select_drzava_po_id_ispravno(self):
        sacuvaj_novu_drzavu("Indija")
        d=dohvati_drzavu_po_id(1)
        self.assertCountEqual([d.id],[1])

    def test_select_drzava_po_id_krivo(self):
        sacuvaj_novu_drzavu('Indija')
        self.assertIsNone(dohvati_drzavu_po_id('ime'))

    def test_update_drzava_ispravno(self):
        sacuvaj_novu_drzavu("Indija")
        azuriraj_drzavu(1,'Austrija')
        dd=procitaj_sve_podatke_drzava()
        for d in dd:
            self.assertCountEqual([(d.id,d.naziv)],[(1,'Austrija')])   

    def test_delete_drzavu(self):
        sacuvaj_novu_drzavu('Indija')
        sacuvaj_novu_drzavu('Austrija')
        izbrisi_drzavu(1)
        dd=procitaj_sve_podatke_drzava()
        for d in dd:
            self.assertCountEqual((d.id,d.naziv), (2,'Austrija'))

    def test_insert_drzavu(self):
        sacuvaj_novu_drzavu('Indija')
        sacuvaj_novu_drzavu('Austrija')
        self.assertCountEqual([dohvati_drzavu_po_nazivu('Indija').id], [1])
        self.assertCountEqual([dohvati_drzavu_po_nazivu('Austrija').id],[2])

    
if __name__=='__main__':
    unittest.main()
