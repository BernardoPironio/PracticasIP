from practicaVI import suma, es_multiplo_de, fahrenheit_a_celsius, doble_si_es_par,es_primo, cantidad_primos_en_rango
import unittest

class test_suma(unittest.TestCase):
    def test_suma_positiva(self):
        self.assertEqual(suma(2,3),5)

    def test_suma_cero(self):
        self.assertEqual(suma(0,0),0)

    def test_suma_negativos(self):
        self.assertEqual(suma(-10,-2),-12)

    def test_suma_positivo_negativo(self):
        self.assertEqual(suma(7,-2),5)

    def test_suma_mal(self):
        self.assertEqual(suma(3,2),5)

class test_doble_si_es_par(unittest.TestCase):
    def test_es_par(self):
        self.assertEqual(doble_si_es_par(2),4)

    def test_no_es_par(self):
        self.assertEqual(doble_si_es_par(1),1)

    def test_es_cero(self):
        self.assertEqual(doble_si_es_par(0),0)

    def test_negativo(self):
        self.assertEqual(doble_si_es_par(-4),-8)

    def test_negativo_no_par(self):
        self.assertEqual(doble_si_es_par(-3),-3)

class test_es_multiplo_de(unittest.TestCase):
    def test_es_multiplo_de_dos(self):
        self.assertTrue(es_multiplo_de(4,2))

    def test_no_es_multiplo_de(self):
        self.assertFalse(es_multiplo_de(4,3))

    def test_es_cero_mutiplo_de(self):
        self.assertTrue(es_multiplo_de(0,13))

class test_fahrenheit_a_celsius(unittest.TestCase):
    def test_farenheit_a_celcius_cualquier(self):
        self.assertAlmostEqual(fahrenheit_a_celsius(10),-12.222,places = 3)

    def test_cero_celcius(self):
        self.assertAlmostEqual(fahrenheit_a_celsius(32),0,places = 5)

    def test_cero_fahrenheit(self):
            self.assertAlmostEqual(fahrenheit_a_celsius(0),-32*(5/9),places = 5)

class test_es_primo(unittest.TestCase):
    def test_es_primo(self):
        self.assertTrue(es_primo(2))

    def test_no_es_primo(self):
            self.assertFalse(es_primo(4))

class test_cantidad_primos_en_rango(unittest.TestCase):
    def test_rango_normal(self):
        self.assertEqual(cantidad_primos_en_rango(2,10),4)

    def test_rango_con_negativo(self):
        self.assertEqual(cantidad_primos_en_rango(-3,4),2)

    def test_rango_dado_vuelta(self):
        self.assertEqual(cantidad_primos_en_rango(8,2),4)

if __name__  == '__main__':
    unittest.main(verbosity= 3)


