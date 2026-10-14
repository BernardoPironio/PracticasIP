from practicaVII import *
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

class test_iguales_consecutivos(unittest.TestCase):
    def test_tiene_al_final(self):
        self.assertTrue(iguales_consecutivos([1,2,3,4,4,6,5,67,67,67]))

    def test_tiene_al_ptincipio(self):
            self.assertTrue(iguales_consecutivos([1,1,1,2,3,4,4,6,5,67]))

    def test_tres_al_final(self):
        self.assertTrue(iguales_consecutivos([1,2,3,4,4,4]))

    def test_no_tiene(self):
        self.assertFalse(iguales_consecutivos([1,1,2,3,3,4,5,6]))

    def test_no_hay_ni_tres(self):
        self.assertFalse(iguales_consecutivos([2,2]))

    def test_justo_tres(self):
         self.assertTrue([1,1,1])

class test_vocales_distintas(unittest.TestCase):
    def test_tiene(self):
        self.assertTrue(vocales_distintas('abcdefghi'))

    def test_no_tiene_tres(self):
              self.assertFalse(vocales_distintas('abcdefgh'))

    def test_todas_vocales(self):
         self.assertTrue(vocales_distintas('aeiou'))

class test_pos_secuencia_ordenada_mas_larga(unittest.TestCase):
    def test_tiene_una_secuencia(self):
        self.assertEqual(pos_secuencia_ordenada_mas_larga([1,2,3,4,5,6,7]),0)

    def test_tiene_dos_secuencias_segunda_larga(self):
            self.assertEqual(pos_secuencia_ordenada_mas_larga([1,2,1,4,5,6,7]),2)

    def test_tiene_una_secuencia_primer_larga(self):
            self.assertEqual(pos_secuencia_ordenada_mas_larga([7,2,3,4,5,1,7]),1)

class test_cantidad_digitos_impares(unittest.TestCase):
    def test_ejemplo_guia(self):
        self.assertEqual(cantidad_digitos_impares([57, 2383, 812, 246]),5)

    def test_sin_impares(self):
        self.assertEqual(cantidad_digitos_impares([22, 2886, 802, 246]),0)

    def test_un_impar(self):
            self.assertEqual(cantidad_digitos_impares([23]),1)

class test_cero_en_posiciones_pares2(unittest.TestCase):
    def test_lista_normal(self):
        self.assertEqual(cero_en_posiciones_pares2([1,2,3,4]),[1,0,3,0])

    def test_lista_uno_solo(self):
        self.assertEqual(cero_en_posiciones_pares2([1]),[1])

    def test_lista_vacia_god(self):
        self.assertEqual(cero_en_posiciones_pares2([]),[])


if __name__  == '__main__':
    unittest.main(verbosity= 3)


