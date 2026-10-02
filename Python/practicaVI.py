from math import sqrt, pi, ceil

'''
  =========================================
  EJERCICIO 1    
  =========================================
'''
# 1
def imprimir_hola_mundo():
    print("¡Hola mundo!")

# 2
def imprimir_un_verso():
    print("Puta, entro escupiendo pura adrenalina, vaciando tinta en la esquina, “garchando” con la más fina, «mirando mal al que mira, tirándole al que me tira, navego entre to’a la mierda, negro, no quiero tu cima. \nAsí que rap, perra, fresh, perra, sé muy bien que me querés tener, perra. Tres perras me esperan,creo que una era tu mujer, nigga.")

# 3
def raizDe2()-> float:
    return round(sqrt(2),4)

# 4 
def factorial_de_dos()-> int:
    return 2

# 5
def perimetro()-> float:
    return 2*pi

'''
  =========================================
  EJERCICIO 2 
  =========================================
'''
# 1
def imprimir_saludo(nombre: str)-> str:
    print(f"Hola {nombre}")

# 2
def raiz_cuadrada_de(n: float)-> float:
    return sqrt(n)

# 3
def fahrenheit_a_celsius(temp_far: float)-> float:
    return (temp_far-32)*(5/9)

# 4
def imprimir_dos_veces(estribillo: str)-> None:
    print(estribillo * 2)

# 5
def es_multiplo_de(n: int, m: int)-> bool:
    return (n % m) == 0

# 6
def es_par(numero: int) -> bool:
    return es_multiplo_de(numero,2)

# 7
def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    porciones_totales = comensales * min_cant_de_porciones
    return ceil(porciones_totales / 8)

'''
  =========================================
  EJERCICIO 3
  =========================================
'''
# 1
def alguno_es_cero(numero1: float, numero2:float)-> bool:
    return numero1 == 0 or numero2 == 0

# 2
def ambos_son_cero(numero1: float, numero2:float)-> bool:
    return numero1 == 0 and numero2 == 0

# 3
def es_nombre_largo(nombre: str)-> bool:
    return 3 <= len(nombre) <= 8

# 4
def es_bisiesto(año: int)-> bool:
    return (año % 400 == 0) or (año % 4 == 0 and año % 100 != 0)

'''
  =========================================
  EJERCICIO 4
  =========================================
'''
# 1
def peso_pino(altura: float)-> float:
    return (min(altura,3)*300) + (max(0,altura-300)*200)

# 2
def es_peso_util(peso: float)-> bool:
    return 400 <= peso <= 1000

# 3
def sirve_pino(altura: float)-> bool:
    return es_peso_util(peso_pino(altura))

'''
  =========================================
  EJERCICIO 5
  =========================================
'''

