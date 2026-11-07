from ejercicios_parcial import *
import unittest

class test_productos_en_stock(unittest.TestCase):

    def test_productos_en_stock_ok(self):
        self.assertEqual(productos_en_stock([("collar", 10), 
                                            ("guau", 5), 
                                            ("collar", 3), 
                                            ("guau", 8), 
                                            ("collar", 15)]), {"collar":(3,15),"guau":(5,8)})

    def test_productos_en_stock_solo_una_vez(self):
        self.assertEqual(productos_en_stock([("collar",3),("correa",4)]),{"collar":(3,3),"correa":(4,4)})


    def test_multiples_cambios_varios_productos(self):
        # El caso clásico con varios productos y subidas/bajadas
        cambios = [
            ("collar", 10), 
            ("guau", 5), 
            ("collar", 3), 
            ("guau", 8), 
            ("collar", 15)
        ]
        resultado = productos_en_stock(cambios)
        esperado = {
            "collar": (3, 15),
            "guau": (5, 8)
        }
        self.assertEqual(resultado, esperado)

    def test_productos_una_sola_vez(self):
        # Si un producto aparece una sola vez, el mínimo y máximo deben ser iguales
        cambios = [("huesito", 12), ("pelota", 4)]
        resultado = productos_en_stock(cambios)
        esperado = {
            "huesito": (12, 12),
            "pelota": (4, 4)
        }
        self.assertEqual(resultado, esperado)

    def test_stock_constante(self):
        # Mismo producto con el mismo stock repetidas veces
        cambios = [("comida", 20), ("comida", 20), ("comida", 20)]
        resultado = productos_en_stock(cambios)
        esperado = {
            "comida": (20, 20)
        }
        self.assertEqual(resultado, esperado)

    def test_fluctuacion_extrema(self):
        # Valores mínimos en cero o variaciones grandes
        cambios = [
            ("shampoo", 50), 
            ("shampoo", 10), 
            ("shampoo", 100), 
            ("shampoo", 0)
        ]
        resultado = productos_en_stock(cambios)
        esperado = {
            "shampoo": (0, 100)
        }
        self.assertEqual(resultado, esperado)

class test_filtrar_codigos_primos(unittest.TestCase):

    def test_filtrar_codigos_primos_ok(self):
        self.assertEqual(filtrar_codigos_primos([34563456345101, 2345234002, 1231212011, 2012022]),[34563456345101, 2345234002, 1231212011])

    def test_filtrar_codigos_primos_ninguno(self):
        self.assertEqual(filtrar_codigos_primos([12312016,213910]),[])

    def test_filtrar_codigos_primos(self):
        self.assertEqual(filtrar_codigos_primos([]),[])

    def test_caso_general_mixto(self,):
        # Una lista con códigos que SÍ y que NO cumplen la condición
        codigos = [12402, 53101, 88804, 91007]
        # 12402 -> termina en 402 (No es primo)
        # 53101 -> termina en 101 (Sí es primo)
        # 88804 -> termina en 804 (No es primo)
        # 91007 -> termina en 007 -> 7 (Sí es primo)
        resultado = filtrar_codigos_primos(codigos)
        esperado = [53101, 91007]
        self.assertEqual(resultado, esperado)

    def test_todos_cumplen(self):
        # Códigos cuyos últimos 3 dígitos son primos
        codigos = [101, 2007, 9017]
        resultado = filtrar_codigos_primos(codigos)
        esperado = [101, 2007, 9017]
        self.assertEqual(resultado, esperado)

    def test_ninguno_cumple(self):
        # Códigos cuyos últimos 3 dígitos NO son primos (pares, divisibles por 5, etc.)
        codigos = [100, 104, 1095] 
        resultado = filtrar_codigos_primos(codigos)
        esperado = []
        self.assertEqual(resultado, esperado)

    def test_ultimos_tres_digitos_primos_chicos_como_cero(self):
        # Números cuyos últimos 3 dígitos arrancan con ceros (ej: 002, 003, 007)
        codigos = [1002, 5003, 9007, 4004]
        # 1002 -> termina en 2 (Primo)
        # 5003 -> termina en 3 (Primo)
        # 9007 -> termina en 7 (Primo)
        # 4004 -> termina en 4 (No es primo)
        resultado = filtrar_codigos_primos(codigos)
        esperado = [1002, 5003, 9007]
        self.assertEqual(resultado, esperado)

class test_subsecuencia_mas_larga(unittest.TestCase):

    def test_subsecuencia_mas_larga_ultimo(self):
        prueba = ["perro","perro","caballo","gato","caballo","perro","gato","perro","perro"]

        self.assertEqual(subsecuencia_mas_larga(prueba),5)

    def test_subsecuencia_mas_larga_una_ultima(self):
        prueba = ["caballo","perro"]

        self.assertEqual(subsecuencia_mas_larga(prueba),1)

    def test_subsecuencia_mas_larga_principio(self):
        prueba = ["gato","perro","caballo","perro"]

        self.assertEqual(subsecuencia_mas_larga(prueba),0)

    def test_subsecuencia_mas_larga_dos_misma_long(self):
        prueba = ["caballo","perro","perro","caballo","gato","gato","caballo"]

        self.assertEqual(subsecuencia_mas_larga(prueba),1)

    def test_caso_general(self):
        # Secuencia mixta donde la más larga está al final o medio
        # "loro" corta la racha
        pacientes = ["perro", "gato", "loro", "perro", "perro", "gato", "hamster"]
        # Las subsecuencias válidas son:
        # 1) ["perro", "gato"] (longitud 2, índice 0)
        # 2) ["perro", "perro", "gato"] (longitud 3, índice 3) -> ¡Esta es la más larga!
        resultado = subsecuencia_mas_larga(pacientes)
        self.assertEqual(resultado, 3)

    def test_mas_larga_al_principio(self):
        # La subsecuencia más larga está al arranque
        pacientes = ["gato", "perro", "gato", "canario", "perro"]
        # ["gato", "perro", "gato"] (longitud 3, índice 0)
        # ["perro"] (longitud 1, índice 4)
        resultado = subsecuencia_mas_larga(pacientes)
        self.assertEqual(resultado, 0)

    def test_empate_de_longitudes(self):
        # Dos subsecuencias válidas del mismo tamaño máximo; debe devolver el índice de la primera
        pacientes = ["perro", "perro", "loro", "gato", "gato"]
        # ["perro", "perro"] (longitud 2, índice 0)
        # ["gato", "gato"] (longitud 2, índice 3)
        # Como empatan, debe ganar la primera (índice 0)
        resultado = subsecuencia_mas_larga(pacientes)
        self.assertEqual(resultado, 0)

    def test_toda_la_lista_valida(self):
        # Toda la lista cumple la condición
        pacientes = ["gato", "perro", "gato", "perro"]
        # La más larga es toda la lista, empieza en el índice 0
        resultado = subsecuencia_mas_larga(pacientes)
        self.assertEqual(resultado, 0)

    def test_un_solo_elemento_valido(self):
        # Por precondición al menos hay un "perro" o "gato"
        pacientes = ["loro", "perro", "loro"]
        # La única subsecuencia válida es ["perro"] en el índice 1
        resultado = subsecuencia_mas_larga(pacientes)
        self.assertEqual(resultado, 1)

class test_un_responsable_por_turno(unittest.TestCase):

    def test_turnos_constantes_ambos_bloques(self):
        # Un día donde la misma persona hace toda la mañana y toda la tarde
        grilla = [
            ["Ana"],    # 9 hs
            ["Ana"],    # 10 hs
            ["Ana"],    # 11 hs
            ["Ana"],    # 12 hs
            ["Carlos"], # 14 hs
            ["Carlos"], # 15 hs
            ["Carlos"], # 16 hs
            ["Carlos"]  # 17 hs
        ]
        resultado = un_responsable_por_turno(grilla)
        esperado = [(True, True)]
        self.assertEqual(resultado, esperado)

    def test_cambio_solo_en_la_manana(self):
        # Dos días: el día 0 tiene un cambio en la mañana, el día 1 es estable
        grilla = [
            ["Luis", "Sofía"],  # 9 hs
            ["Luis", "Sofía"],  # 10 hs
            ["Pedro", "Sofía"], # 11 hs -> ¡Cambio en el día 0!
            ["Luis", "Sofía"],  # 12 hs
            ["Juan", "Mateo"],  # 14 hs
            ["Juan", "Mateo"],  # 15 hs
            ["Juan", "Mateo"],  # 16 hs
            ["Juan", "Mateo"]   # 17 hs
        ]
        resultado = un_responsable_por_turno(grilla)
        esperado = [(False, True), (True, True)]
        self.assertEqual(resultado, esperado)

    def test_cambio_solo_en_la_tarde(self):
        # Mañana constante en ambos días, pero el día 1 tiene un cambio en la tarde
        grilla = [
            ["Ana", "Ana"],
            ["Ana", "Ana"],
            ["Ana", "Ana"],
            ["Ana", "Ana"],
            ["Carlos", "Carlos"],
            ["Carlos", "Sofía"], # 15 hs -> ¡Cambio en el día 1!
            ["Carlos", "Carlos"],
            ["Carlos", "Carlos"]
        ]
        resultado = un_responsable_por_turno(grilla)
        esperado = [(True, True), (True, False)]
        self.assertEqual(resultado, esperado)

    def test_cambios_en_ambos_turnos(self):
        # Jornadas con cambios tanto en la mañana como en la tarde
        grilla = [
            ["Ana", "Luis"],
            ["Bea", "Luis"], # Cambio en la mañana del día 0
            ["Ana", "Luis"],
            ["Ana", "Luis"],
            ["Carlos", "Sofía"],
            ["Carlos", "Sofía"],
            ["Carlos", "Raúl"], # Cambio en la tarde del día 1
            ["Carlos", "Sofía"]
        ]
        resultado = un_responsable_por_turno(grilla)
        esperado = [(False, True), (True, False)]
        self.assertEqual(resultado, esperado)

class test_promedio_de_salidas(unittest.TestCase):

    def test_caso_general_mixto(self):
        # Amigos con una mezcla de éxitos (1-60), fracasos (61) y ausencias (0)
        registro = {
            "Ana": [45, 61, 30],
            "Luis": [0, 61, 0]
        }
        resultado = promedio_de_salidas(registro)
        esperado = {
            "Ana": (2, 37.5),
            "Luis": (0, 0.0)
        }
        self.assertEqual(resultado, esperado)

    def test_todas_exitosas(self):
        # Una persona que salió de todas las salas con buenos tiempos
        registro = {
            "Carlos": [20, 40, 60]
        }
        resultado = promedio_de_salidas(registro)
        # Cantidad: 3, Promedio: (20 + 40 + 60) / 3 = 120 / 3 = 40.0
        esperado = {
            "Carlos": (3, 40.0)
        }
        self.assertEqual(resultado, esperado)

    def test_ninguna_salida_exitosa_con_ceros_y_61(self):
        # Persona que solo tiene ceros (no fue) o 61 (no pudo salir)
        registro = {
            "Sofia": [0, 61, 61, 0]
        }
        resultado = promedio_de_salidas(registro)
        # Cantidad: 0, Promedio forzado a 0.0 por el enunciado
        esperado = {
            "Sofia": (0, 0.0)
        }
        self.assertEqual(resultado, esperado)

    def test_una_sola_sala_exitosa(self):
        # Persona con una única sala de la cual salió con éxito
        registro = {
            "Majo": [50]
        }
        resultado = promedio_de_salidas(registro)
        # Cantidad: 1, Promedio: 50.0
        esperado = {
            "Majo": (1, 50.0)
        }
        self.assertEqual(resultado, esperado)

class test_tiempo_mas_rapido(unittest.TestCase):

  def test_caso_general_multiples_validos(self):
    # El tiempo más rápido es 30 (repetido). Debe devolver la de menor índice (1)
    tiempos_salas = [45, 30, 50, 30]
    resultado = tiempo_mas_rapido(tiempos_salas)
    esperado = 1
    self.assertEqual(resultado, esperado)

  def test_invalidos_intercalados(self):
    # Excluye 0 y 61. Entre los válidos (25 en ind 2 y 60 en ind 3), el menor es 25
    tiempos_salas = [0, 61, 25, 60, 0]
    resultado = tiempo_mas_rapido(tiempos_salas)
    esperado = 2
    self.assertEqual(resultado, esperado)

  def test_unico_elemento_valido(self):
    # Solo un tiempo válido entre 1 y 60 inclusivo
    tiempos_salas = [0, 0, 42, 61]
    resultado = tiempo_mas_rapido(tiempos_salas)
    esperado = 2
    self.assertEqual(resultado, esperado)

  def test_minimo_al_inicio(self):
    # El tiempo más rápido (15) está en la primera posición (índice 0)
    tiempos_salas = [15, 55, 40, 20]
    resultado = tiempo_mas_rapido(tiempos_salas)
    esperado = 0
    self.assertEqual(resultado, esperado)

  def test_minimo_al_final(self):
    # El tiempo más rápido (10) está en la última posición (índice 3)
    tiempos_salas = [50, 45, 60, 10]
    resultado = tiempo_mas_rapido(tiempos_salas)
    esperado = 3
    self.assertEqual(resultado, esperado)

  def test_valores_limites_rango(self):
    # Evalúa en las fronteras inclusivas del rango válido (1 y 60)
    tiempos_salas = [60, 1, 35]
    resultado = tiempo_mas_rapido(tiempos_salas)
    esperado = 1
    self.assertEqual(resultado, esperado)

class test_racha_mas_larga(unittest.TestCase):

  def test_racha_en_el_medio(self):
    # Racha exitosa más larga en el medio ([30, 45, 20] de longitud 3)
    tiempos = [0, 30, 45, 20, 61, 15]
    resultado = racha_mas_larga(tiempos)
    esperado = (1, 3)
    self.assertEqual(resultado, esperado)

  def test_empate_devuelve_primera(self):
    # Hay dos rachas de igual longitud máxima (2): [10, 20] y [40, 50]. Debe devolver la primera (0, 1)
    tiempos = [10, 20, 0, 40, 50]
    resultado = racha_mas_larga(tiempos)
    esperado = (0, 1)
    self.assertEqual(resultado, esperado)

  def test_racha_unica_de_un_elemento(self):
    # Una única salida exitosa aislada por ceros y 61, la racha es de longitud 1 (índice 2 a 2)
    tiempos = [0, 61, 42, 0, 61]
    resultado = racha_mas_larga(tiempos)
    esperado = (2, 2)
    self.assertEqual(resultado, esperado)

  def test_toda_la_lista_exitosa(self):
    # Toda la secuencia completa es una racha exitosa
    tiempos = [15, 30, 45, 60]
    resultado = racha_mas_larga(tiempos)
    esperado = (0, 3)
    self.assertEqual(resultado, esperado)

  def test_racha_al_final(self):
    # La racha más larga se encuentra al final de la lista
    tiempos = [0, 61, 10, 25, 40]
    resultado = racha_mas_larga(tiempos)
    esperado = (2, 4)
    self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()