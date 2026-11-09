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

class TestEscapeEnSolitario(unittest.TestCase):
    
    def test_varias_salas_mixtas(self):
        """Verifica una matriz con múltiples salas donde algunas cumplen y otras no."""
        amigos_por_salas = [
            [0, 0, 30, 0],   # Índice 0: Cumple (1°, 2° y 4° en 0; 3° fue en 30)
            [10, 0, 20, 0],  # Índice 1: No cumple (el 1° amigo fue)
            [0, 0, 0, 0],    # Índice 2: No cumple (el 3° amigo no fue: 0)[cite: 1]
            [0, 0, 61, 0],   # Índice 3: Cumple (3° no salió: 61, pero fue)[cite: 1]
            [0, 5, 40, 0]    # Índice 4: No cumple (el 2° amigo fue)[cite: 1]
        ]
        resultado = escape_en_solitario(amigos_por_salas)
        self.assertEqual(resultado, [0, 3])

    def test_ninguna_sala_cumple(self):
        """Verifica el caso donde ninguna sala cumple la condición[cite: 1]."""
        amigos_por_salas = [
            [10, 20, 30, 40],
            [0, 0, 0, 0],
            [5, 0, 50, 0]
        ]
        resultado = escape_en_solitario(amigos_por_salas)
        self.assertEqual(resultado, [])

    def test_todas_las_salas_cumplen(self):
        """Verifica una matriz donde todas las salas cumplen la condición[cite: 1]."""
        amigos_por_salas = [
            [0, 0, 25, 0],
            [0, 0, 61, 0],  # No salió, pero fue
            [0, 0, 1, 0]    # Salió rápido
        ]
        resultado = escape_en_solitario(amigos_por_salas)
        self.assertEqual(resultado, [0, 1, 2])

    def test_sala_unica_que_cumple(self):
        """Verifica una matriz con una sola sala que sí cumple la condición[cite: 1]."""
        amigos_por_salas = [
            [0, 0, 45, 0]
        ]
        resultado = escape_en_solitario(amigos_por_salas)
        self.assertEqual(resultado, [0])

    def test_sala_unica_que_no_cumple(self):
        """Verifica una matriz con una sola sala donde el tercer amigo tampoco fue[cite: 1]."""
        amigos_por_salas = [
            [0, 0, 0, 0]
        ]
        resultado = escape_en_solitario(amigos_por_salas)
        self.assertEqual(resultado, [])

class TestTorneoDeGallinas(unittest.TestCase):
    
    def test_dos_jugadores_mixtos(self):
        """Verifica un torneo básico de 2 jugadores con estrategias opuestas[cite: 2]."""
        estrategias = {
            "Ana": "me desvío siempre",
            "Beto": "me la banco y no me desvío"
        }
        # Ana se desvía (-15), Beto no se desvía (+10)[cite: 2]
        resultado = torneo_de_gallinas(estrategias)
        esperado = {
            "Ana": -15,
            "Beto": 10
        }
        self.assertEqual(resultado, esperado)

    def test_todos_se_desvian(self):
        """Verifica un torneo donde todos eligen desviarse siempre[cite: 2]."""
        estrategias = {
            "Ana": "me desvío siempre",
            "Beto": "me desvío siempre",
            "Carlos": "me desvío siempre"
        }
        # Hay 3 enfrentamientos en total: (Ana-Beto, Ana-Carlos, Beto-Carlos).
        # En cada uno ambos pierden 10 puntos, por lo que cada jugador acumula -20[cite: 2].
        resultado = torneo_de_gallinas(estrategias)
        esperado = {
            "Ana": -20,
            "Beto": -20,
            "Carlos": -20
        }
        self.assertEqual(resultado, esperado)

    def test_todos_se_la_bancan(self):
        """Verifica un torneo donde todos deciden no desviarse nunca[cite: 2]."""
        estrategias = {
            "Ana": "me la banco y no me desvío",
            "Beto": "me la banco y no me desvío",
            "Carlos": "me la banco y no me desvío"
        }
        # 3 enfrentamientos. En cada choque ambos pierden 5 puntos -> cada uno acumula -10[cite: 2].
        resultado = torneo_de_gallinas(estrategias)
        esperado = {
            "Ana": -10,
            "Beto": -10,
            "Carlos": -10
        }
        self.assertEqual(resultado, esperado)

    def test_torneo_mixto_varios_jugadores(self):
        """Verifica un escenario heterogéneo con múltiples jugadores y distintas combinaciones[cite: 2]."""
        estrategias = {
            "Ana": "me desvío siempre",
            "Beto": "me la banco y no me desvío",
            "Carlos": "me desvío siempre"
        }
        # Enfrentamientos:
        # 1. Ana (desvía) vs Beto (no desvía) -> Ana: -15, Beto: +10[cite: 2]
        # 2. Ana (desvía) vs Carlos (desvía) -> Ana: -10, Carlos: -10[cite: 2]
        # 3. Beto (no desvía) vs Carlos (desvía) -> Beto: +10, Carlos: -15[cite: 2]
        # Totales:
        # Ana = -15 + (-10) = -25
        # Beto = 10 + 10 = 20
        # Carlos = -10 + (-15) = -25
        resultado = torneo_de_gallinas(estrategias)
        esperado = {
            "Ana": -25,
            "Beto": 20,
            "Carlos": -25
        }
        self.assertEqual(resultado, esperado)

# Función auxiliar interna solo para comparar el contenido de las colas en los tests
def _cola_a_lista(cola: Cola) -> list:
    elementos = []
    aux = Cola()
    while not cola.empty():
        elem = cola.get()
        elementos.append(elem)
        aux.put(elem)
    while not aux.empty():
        cola.put(aux.get())
    return elementos

class TestColaEnElBanco(unittest.TestCase):
    
    def test_reordenar_mixto(self):
        """Verifica una cola con clientes VIP y comunes intercalados[cite: 3]."""
        fila_original = Cola()
        datos_entrada = [("Ana", "común"), ("Beto", "vip"), ("Carlos", "común"), ("Diana", "vip")]
        for item in datos_entrada:
            fila_original.put(item)
            
        res = reordenar_cola_priorizando_vips(fila_original)
        
        # Los VIPs deben quedar primero manteniendo su orden, seguidos de los comunes[cite: 3]
        self.assertEqual(_cola_a_lista(res), ["Beto", "Diana", "Ana", "Carlos"])
        
        # Corroboramos que la cola original (parámetro in) NO se modificó
        self.assertEqual(_cola_a_lista(fila_original), datos_entrada)

    def test_solo_vips(self):
        """Verifica una cola donde todos los clientes son VIP[cite: 3]."""
        fila_original = Cola()
        datos_entrada = [("Zoe", "vip"), ("Julian", "vip"), ("Lucía", "vip")]
        for item in datos_entrada:
            fila_original.put(item)
            
        res = reordenar_cola_priorizando_vips(fila_original)
        
        self.assertEqual(_cola_a_lista(res), ["Zoe", "Julian", "Lucía"])
        self.assertEqual(_cola_a_lista(fila_original), datos_entrada)

    def test_solo_comunes(self):
        """Verifica una cola donde todos los clientes son comunes[cite: 3]."""
        fila_original = Cola()
        datos_entrada = [("Pedro", "común"), ("Sofía", "común")]
        for item in datos_entrada:
            fila_original.put(item)
            
        res = reordenar_cola_priorizando_vips(fila_original)
        
        self.assertEqual(_cola_a_lista(res), ["Pedro", "Sofía"])
        self.assertEqual(_cola_a_lista(fila_original), datos_entrada)

    def test_orden_relativo_respetado(self):
        """Verifica que el orden interno de cada categoría se mantenga estricto[cite: 3]."""
        fila_original = Cola()
        datos_entrada = [
            ("Cliente1", "común"),
            ("VIP1", "vip"),
            ("Cliente2", "común"),
            ("VIP2", "vip"),
            ("VIP3", "vip")
        ]
        for item in datos_entrada:
            fila_original.put(item)
            
        res = reordenar_cola_priorizando_vips(fila_original)
        
        self.assertEqual(_cola_a_lista(res), ["VIP1", "VIP2", "VIP3", "Cliente1", "Cliente2"])
        self.assertEqual(_cola_a_lista(fila_original), datos_entrada)

class test_cuantos_sufijos_son_palindromos(unittest.TestCase):

    def test_ejemplo_consigna(self):
        # Ej: "Diego" -> sufijos: "Diego", "iego", "ego", "go", "o"
        # De estos, solo "o" es palíndromo (longitud 1) -> Total: 1
        texto = "Diego"
        resultado = cuantos_sufijos_son_palindromos(texto)
        esperado = 1
        self.assertEqual(resultado, esperado)

    def test_sufijos_neuquen(self):
        # Texto: "neuquen" -> sufijos: 
        # "neuquen" (sí, es palíndromo), "euquen" (no), "uquen" (no), 
        # "quen" (no), "uen" (no), "en" (no), "n" (sí, una sola letra) -> Total: 2
        texto = "neuquen"
        resultado = cuantos_sufijos_son_palindromos(texto)
        esperado = 2
        self.assertEqual(resultado, esperado)

    def test_todos_palindromos(self):
        # Texto: "aba" -> sufijos: "aba" (sí), "ba" (no), "a" (sí) -> Total: 2
        texto = "aba"
        resultado = cuantos_sufijos_son_palindromos(texto)
        esperado = 2
        self.assertEqual(resultado, esperado)

    def test_una_sola_letra(self):
        # Texto: "a" -> sufijos: "a" (sí) -> Total: 1
        texto = "a"
        resultado = cuantos_sufijos_son_palindromos(texto)
        esperado = 1
        self.assertEqual(resultado, esperado)

class test_quien_gano_el_tateti_facilito(unittest.TestCase):

    def test_gana_ana(self):
        # Tablero de 5x5 donde Ana ("X") consigue 3 seguidas en forma vertical (columna 1)
        # Res esperado: 1 (gana Ana)
        tablero = [
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", "X"],
            [" ", " ", " ", " ", "X"],
            [" ", " ", " ", " ", "X"]
        ]
        resultado = quien_gano_el_tateti_facilito(tablero)
        esperado = 1
        self.assertEqual(resultado, esperado)

    def test_gana_beto(self):
        # Tablero de 5x5 donde Beto ("O") consigue 3 seguidas en forma vertical (columna 2)
        # Res esperado: 2 (gana Beto)
        tablero = [
            ["X", " ", "O", " ", " "],
            ["X", " ", "O", " ", " "],
            [" ", " ", "O", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "]
        ]
        resultado = quien_gano_el_tateti_facilito(tablero)
        esperado = 2
        self.assertEqual(resultado, esperado)

    def test_empate_o_en_curso(self):
        # Tablero de 5x5 sin tres en raya vertical para nadie
        # Res esperado: 0 (nadie ganó)
        tablero = [
            ["X", "O", " ", " ", " "],
            [" ", "O", "X", " ", " "],
            ["X", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "]
        ]
        resultado = quien_gano_el_tateti_facilito(tablero)
        esperado = 0
        self.assertEqual(resultado, esperado)

    def test_trampa_de_beto(self):
        # Tablero donde Ana gana verticalmente y Beto también hace 3 verticales después (hizo trampa)
        # Res esperado: 3 (ganaron ambos, evidencia trampa)
        tablero = [
            ["X", "O", " ", " ", " "],
            ["X", "O", " ", " ", " "],
            ["X", "O", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "]
        ]
        resultado = quien_gano_el_tateti_facilito(tablero)
        esperado = 3
        self.assertEqual(resultado, esperado)

class test_orden_de_atencion(unittest.TestCase):

    def test_intercalado_simple(self):
        # Urgentes: [1, 2] | Postergables: [10, 20]
        # Esperado: 1, 10, 2, 20
        urgentes = Cola()
        for x in [1, 2]:
            urgentes.put(x)

        postergables = Cola()
        for x in [10, 20]:
            postergables.put(x)

        resultado = orden_de_atencion(urgentes, postergables)
        
        esperado = Cola()
        for x in [1, 10, 2, 20]:
            esperado.put(x)

        self.assertEqual(list(resultado.queue), list(esperado.queue))

    def test_un_solo_elemento(self):
        # Urgentes: [5] | Postergables: [99]
        # Esperado: 5, 99
        urgentes = Cola()
        urgentes.put(5)

        postergables = Cola()
        postergables.put(99)

        resultado = orden_de_atencion(urgentes, postergables)
        
        esperado = Cola()
        for x in [5, 99]:
            esperado.put(x)

        self.assertEqual(list(resultado.queue), list(esperado.queue))

    def test_varios_elementos(self):
        # Urgentes: [100, 200, 300] | Postergables: [1, 2, 3]
        # Esperado: 100, 1, 200, 2, 300, 3
        urgentes = Cola()
        for x in [100, 200, 300]:
            urgentes.put(x)

        postergables = Cola()
        for x in [1, 2, 3]:
            postergables.put(x)

        resultado = orden_de_atencion(urgentes, postergables)
        
        esperado = Cola()
        for x in [100, 1, 200, 2, 300, 3]:
            esperado.put(x)

        self.assertEqual(list(resultado.queue), list(esperado.queue))

class test_alarma_epidemiologica(unittest.TestCase):

    def test_supera_umbral(self):
        # Registros: 4 atenciones en total
        # - "gripe": 3 pacientes (75% o 0.75)
        # - "covid": 1 paciente (25% o 0.25)
        # Infecciosas: ["gripe", "covid"]
        # Umbral: 0.5 (50%)
        # Esperado: solo "gripe" supera el umbral (0.75)
        registros = [
            (101, "gripe"),
            (102, "gripe"),
            (103, "gripe"),
            (104, "covid")
        ]
        infecciosas = ["gripe", "covid"]
        umbral = 0.5

        resultado = alarma_epidemiologica(registros, infecciosas, umbral)
        esperado = {"gripe": 0.75}

        self.assertEqual(resultado, esperado)

    def test_ninguna_supera_umbral(self):
        # Umbral alto (0.8), ninguna enfermedad alcanza el 80% de los casos
        registros = [
            (1, "gripe"),
            (2, "gripe"),
            (3, "dengue"),
            (4, "covid")
        ]
        infecciosas = ["gripe", "dengue", "covid"]
        umbral = 0.8

        resultado = alarma_epidemiologica(registros, infecciosas, umbral)
        esperado = {}

        self.assertEqual(resultado, esperado)

    def test_solo_enfermedades_infecciosas(self):
        # Hay registros de una enfermedad que NO está en la lista de infecciosas ("resfrio").
        # No debe aparecer en el resultado aunque supere el umbral.
        registros = [
            (1, "resfrio"),
            (2, "resfrio"),
            (3, "resfrio"),
            (4, "gripe")
        ]
        infecciosas = ["gripe"]
        umbral = 0.2

        resultado = alarma_epidemiologica(registros, infecciosas, umbral)
        esperado = {"gripe": 0.25}  # 1 de 4 registros para "gripe" (25%)

        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()