import unittest
from practicaVIII import *

class test_calcularPromedioPorEstudiante(unittest.TestCase):

    def test_lista_vacia(self):
        self.assertEqual(calcular_promedio_por_estudiante([]),{})

    
    def test_ok(self):
        self.assertEqual(calcular_promedio_por_estudiante([]),{})

if __name__  == '__main__':
    unittest.main(verbosity= 3)
