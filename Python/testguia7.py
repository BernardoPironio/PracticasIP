from practicaVII import suma_total, PalabrasUnidas
import unittest

class test_suma_total(unittest.TestCase):
    def test_lista_vacia(self):
        self.assertEqual(suma_total([]),0)

    def test_un_elemento(self):
        self.assertEqual(suma_total([13]),13)

    def test_mas_de_uno(self):
        self.assertEqual(suma_total([1,2,-3,6]),6)

class test_PalabrasUnidas(unittest.TestCase):
    def test_sin_palabras(self):
        self.assertEqual(PalabrasUnidas([]),'')

    def test_normal(self):
        self.assertEqual(PalabrasUnidas(['bernie','agus','juan']),'bernie agus juan')

    def test_vacios(self):
        self.assertEqual(PalabrasUnidas(['','']),' ')

    def test_espacios(self):
            self.assertEqual(PalabrasUnidas([' ',' ']),'   ')

if __name__  == '__main__':
    unittest.main(verbosity= 3)


