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
# 1
def doble_si_es_par(numero: int)-> int:
    if numero % 2 == 0:
        return numero*2
    else:
        return numero

# 2
def devolver_valor_si_es_par_si_no_el_que_sigue(numero: int)-> int:
    if numero % 2 == 0:
        return numero
    else:
        return numero + 1

# 3 
def doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int)-> int:
    if numero % 9 == 0:
        return 3*numero
    elif numero % 3 == 0:
        return 2*numero
    else:
        return numero

# 4
def lindo_nombre(nombre: str)-> str:
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras"
    else:
        return "Tu nombre tiene menos que 5 letras"

# 5
def elRango(numero: int)-> str:
    if numero < 5:
        return "Menor a 5"
    elif 10 < numero < 20:
        return "Entre 10 y 20"
    elif numero > 20:
        return "Mayor a 20" 

# 6
def vacaciones(sexo: str, edad: int)-> str:
    sexo = sexo.upper()
    if edad <= 18 or (sexo == "M" and edad >= 65) or (sexo == "F" and edad >= 60): 
        return "Andá de vacaciones" 
    else: 
        return "Te toca trabajar"

'''
  =========================================
  EJERCICIO 6
  =========================================
'''
# 1
def numeros_uno_al_diez():
    n = 1
    while n <= 10:
        print(n) 
        n += 1

# 2
def pares_del_10_al_40():
    n = 10
    while n <= 40:
        print(n)
        n += 2

# 3
def eco():
    n = 1
    while n <= 10:
        print("eco") 
        n += 1

# 4
def despegue(n: int):
    while n >= 1:
        print(n)
        n -= 1
    else:
        print("Despegue")

# 5
def viaje_en_tiempo(partida: int, llegada: int):
    while partida > llegada:
        print(f"Viajó uno año al pasado, estamos en el año {partida - 1}")
        partida -= 1

# 6
def viaje_en_tiempo_aristóteles(partida: int):
    actual = partida
    while actual - 20 > -384:
        print(f"Viajó 20 años al pasado, estamos en el año {actual - 20}")
        actual -= 20

'''
  =========================================
  EJERCICIO 7
  =========================================
'''
# 1
def numeros_uno_al_diez_range():
    for n in range(1,11):
        print(n)

# 2
def pares_del_10_al_40_range():
    for i in range(10,41,2):
        print(i)

# 3
def eco_range():
    for i in range(1,11):
        print("eco")

# 4
def despegue_range(n: int):
    for i in range(n,0,-1):
        print(i)
    print("Despegue")

# 5
def viaje_en_tiempo_range(partida: int, llegada: int):
    for i in range(partida-1,llegada - 1,-1):
        print(f"Viajó un año al pasado, estamos en el año: {i}")

# 6
def viaje_en_tiempo_aristóteles_range(partida: int):
    for i in range(partida - 20, -384 - 1,-20):
        print(f"Viajó 20 años al pasado, estamos en el año {i}")


'''
  =========================================
  EJERCICIOS CLASE  
  =========================================
'''
# suma
def suma(a: int, b: int)-> int:
    return a + b

# pitagorica
def triada_pitagorica(a: int, b:int, c: int)-> bool:
    return a**2 + b**2 == c**2

# primo
def es_primo(n: int)-> bool:
    k = n - 1
    if n < 2:
        return False
    while k > 1:
        if n % k == 0:
            return False
        k -= 1
    else:
        return True

# cantidad de primos
def cantidad_primos_en_rango(m: int, n :int)-> int:
    res: int = 0
    if m <= n:
        for i in range(m,n + 1,1):
            if es_primo(i):
                res += 1
    else:
        for i in range(n,m + 1):
            if es_primo(i):
                res += 1
    return res