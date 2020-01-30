import sys
import os
import unittest
from itertools import permutations
if __name__=='__main__':
    sys.path.append(os.path.abspath(".."))
from Entiteti.poruka import Poruka

class TestTrokut(unittest.TestCase):
    def test_init_type_error_string_arg(self):
        with self.assertRaises(TypeError):
            Poruka(1,"Hello","r",3,0)
    def test_init_type_error_string_arg_2(self):
        with self.assertRaises(TypeError):
            Poruka(1,"Hello",3,"r",0)
    def test_init_type_error_string_arg_3(self):
        with self.assertRaises(TypeError):
            Poruka(1,"Hello",2,3,0)
    
if __name__=='__main__':
    unittest.main()