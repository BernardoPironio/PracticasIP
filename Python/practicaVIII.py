from typing import TextIO
import random
from queue import LifoQueue as Pila 
from queue import Queue as Cola

'''
  =========================================
  EJERCICIO 1
  =========================================
'''
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    p = Pila()
    for _ in range(cantidad):
        p.put(random.randint(desde,hasta))

    return p

'''
  =========================================
  EJERCICIO 2
  =========================================
'''
def cantidad_elementos(p: Pila) -> int:
    pila_aux: Pila = Pila()
    contador: int = 0

    while not p.empty():
        elemento = p.get()
        pila_aux.put(elemento)
        contador += 1

    while not pila_aux.empty():
        elemento = pila_aux.get()
        p.put(elemento)

    return contador

'''
  =========================================
  EJERCICIO 3
  =========================================
'''
def buscar_el_maximo(p: Pila[int]) -> int:
    pila_aux: Pila[int] = Pila()
    maximo: int = p.get()
    pila_aux.put(maximo)

    while not p.empty():
        actual: int = p.get()

        if maximo < actual:
            maximo = actual
            pila_aux.put(actual)
        else:
            pila_aux.put(actual)

    while not pila_aux.empty():
        elemento = pila_aux.get()
        p.put(elemento)

    return maximo

'''
  =========================================
  EJERCICIO 4
  =========================================
'''
def buscar_nota_max(p: Pila[tuple[str,int]]) -> tuple[str,int]:
    pila_aux: Pila[tuple[str,int]] = Pila()
    maximo: int = p.get()
    pila_aux.put(maximo)

    while not p.empty():
        tupla_actual: tuple[str,int] = p.get()

        if maximo[1] < tupla_actual[1]:
            maximo = tupla_actual
            pila_aux.put(tupla_actual)
        else:
            pila_aux.put(tupla_actual)

    while not pila_aux.empty():
        elemento = pila_aux.get()
        p.put(elemento)

    return maximo

'''
  =========================================
  EJERCICIO 5
  =========================================
'''
def esta_bien_balanceada(s: str) -> bool:
    pila = Pila()

    for caracter in s:

        if caracter == '(':
            pila.put(caracter) 
        elif caracter == ')':
            if pila.empty():
                return False
            pila.get()          
            
    return pila.empty()

'''
  =========================================
  EJERCICIO 6
  =========================================
'''
def evaluar_expresion(s: str) -> float:
    resultado: str = Pila()
    operadores = ['-','+','*','/']
    for e in s:
        if e not in operadores and e != ' ':
            resultado.put(e)
        elif e == '-':
            segundo: int = int(resultado.get())
            primero: int = int(resultado.get())
            token: float = primero - segundo
            resultado.put(token)
        elif e == '+':
            segundo: int = int(resultado.get())
            primero: int = int(resultado.get())
            token: float = primero + segundo
            resultado.put(token)
        elif e == '*':
            segundo: int = int(resultado.get())
            primero: int = int(resultado.get())
            token: float = primero * segundo
            resultado.put(token)
        elif e == '/':
            segundo: int = int(resultado.get())
            primero: int = int(resultado.get())
            token: float = primero / segundo
            resultado.put(token)
        else: 
            pass
    return resultado.get()

'''
  =========================================
  EJERCICIO 7
  =========================================
'''
def intercalar(p1: Pila, p2: Pila) -> Pila:
    pila_aux: Pila = Pila()
    intercalada: Pila = Pila()

    while not p1.empty():
        elemento1 = p1.get()
        elemento2 = p2.get()
        pila_aux.put(elemento2)
        pila_aux.put(elemento1)

    while not pila_aux.empty():
        elemento = pila_aux.get()
        intercalada.put(elemento)
        
    return intercalada

'''
  =========================================
  EJERCICIO 8
  =========================================
'''
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola:
    cola: Cola = Cola()

    for _ in range(cantidad):
        cola.put(random.randint(desde,hasta))

    return cola

'''
  =========================================
  EJERCICIO 9
  =========================================
'''
def cantidad_de_elementos(c: Cola) -> int:
    cola_aux: Cola = Cola()
    cantidad: int = 0

    while not c.empty():
        elemento = c.get()
        cola_aux.put(elemento)
        cantidad += 1

    while not cola_aux.empty():
        elemento = cola_aux.get()
        c.put(elemento)

    return cantidad

'''
  =========================================
  EJERCICIO 10
  =========================================
'''
def buscar_el_maximo(c: Cola) -> int:
    cola_aux: Cola = Cola()
    maximo: int = cola.get()
    cola_aux.put(maximo)

    while not c.empty():
        proximo: int = c.get()

        if maximo < proximo:
            maximo = proximo

        cola_aux.put(proximo)

    while not cola_aux.empty():
        elemento = cola_aux.get()
        c.put(elemento)

    return maximo
        
'''
  =========================================
  EJERCICIO 11
  =========================================
'''
def buscar_nota_minima(c: Cola[tuple[str,int]]) ->  tuple[str,int]:
    cola_aux: Cola = Cola()
    minimo: tuple[str,int] = c.get()
    cola_aux.put(minimo)

    while not c.empty():
        proximo: tuple[str,int] = c.get()
        cola_aux.put(proximo)

        if minimo > proximo:
            minimo = proximo

    while not cola_aux.empty():
        elemento = cola_aux.get()
        c.put(elemento)

    return minimo

'''
  =========================================
  EJERCICIO 12
  =========================================
'''
def intercalar(c1: Cola, c2: Cola) -> Cola:
    intercalada: Cola = Cola()

    while not c2.empty():
        elemento1 = c1.get()
        elemento2 = c2.get()

        intercalada.put(elemento1)
        intercalada.put(elemento2)

    return intercalada

'''
  =========================================
  EJERCICIO 13
  =========================================
'''
# 1
def armar_secuencia_de_bingo() -> Cola:
    disponibles: list[int] = list(range(100))
    cola: Cola = Cola()

    while len(disponibles) > 0:
        n = disponibles.pop(random.randint(0,len(disponibles)-1))
        cola.put(n)

    return cola

# 2
def jugar_carton_de_bingo(carton: list[int],bolillero: Cola[int]) -> int:
    contador: int = 0
    cantidad_salieron: int = 0

    while cantidad_salieron != 12:
        bola: int = bolillero.get()
        contador += 1

        if bola in carton:
            cantidad_salieron += 1

    return contador

'''
  =========================================
  EJERCICIO 14
  =========================================
'''
def pacientes_urgentes(c: Cola[tuple[int,str,str]]) -> int:
    cola_aux: Cola = Cola()
    contador: int = 0

    while not c.empty():
        elemento = c.get()
        cola_aux.put(elemento)

        if elemento[0] < 4:
            contador += 1

    while not cola_aux.empty():
        elemento = cola_aux.get()
        c.put(elemento)

    return contador

'''
  =========================================
  EJERCICIO 15
  =========================================
'''
def atencion_clientes(c: Cola[tuple[str,int,bool,bool]]) -> Cola[tuple[str,int,bool,bool]]:
    cola_aux: Cola = Cola()
    cola_no_prioridad: Cola = Cola()
    cola_no_preferencial: Cola = Cola()
    nueva: Cola = Cola()

    while not c.empty():
        elemento = c.get()
        cola_aux.put(elemento)

        if not elemento[3]:
            cola_no_prioridad.put(elemento)
        else:
            nueva.put(elemento)

    while not cola_no_prioridad.empty():
        elemento = cola_no_prioridad.get()

        if not elemento[2]:
            cola_no_preferencial.put(elemento)
        else: 
            nueva.put(elemento)

    while not cola_no_preferencial.empty():
        elemento = cola_no_preferencial.get()
        nueva.put(elemento)

    return nueva

'''
  =========================================
  EJERCICIO 16
  =========================================
'''
def calcular_promedio_por_estudiante(notas: list[tuple[str, float]]) -> dict[str:float]:
    lista_notas_por_persona: dict[str,list[float]] = {}

    for (nombre,nota) in notas:
        if nombre not in lista_notas_por_persona.keys():
            lista_notas_por_persona[nombre] = [nota]
        else:
            lista_notas_por_persona[nombre].append(nota) 

    res: dict[str,float] = {}

    for nombre in lista_notas_por_persona.keys():
        res[nombre] = 0
        for n in lista_notas_por_persona[nombre]:
            res[nombre] += n
        res[nombre] = res[nombre]/len(lista_notas_por_persona[nombre])
    return res

'''
  =========================================
  EJERCICIO 17
  =========================================
'''

        
'''
  =========================================
  EJERCICIO 19
  =========================================
'''
# 1
def contar_lineas(nombre_archivo: str) -> int:
    archivo: TextIO = open(nombre_archivo, 'r')
    lineas: list[str] = archivo.readlines()
    archivo.close()
    cant_lineas: int = len(lineas)
    return cant_lineas

'''
  =========================================
  EJERCICIO 22
  =========================================
'''
def es_comentario(linea: str):
    if linea[0] == "#":
        res: bool = True

    for caracter in linea:
        if caracter != " ":
            pass
        elif caracter == "#":
            res: bool = False
            

    return res

def clonar_sin_comentarios(nombre_archivo_entrada: str,nombre_archivo_salida: str) -> None:
    archivo_r: TextIO = open(nombre_archivo_entrada, 'r')
    archivo_w: TextIO = open(nombre_archivo_salida,'w')
    lineas: list[str] = archivo_r.readlines()
    archivo_r.close()



    archivo_w.close()

'''
  =========================================
  EJERCICIO 20
  =========================================
'''
def palabras_de_linea(linea: str) -> list[str]:
    palabras = []
    palabra = "" 
    
    for caracter in linea:
        if caracter != " ":
            palabra += caracter
        elif palabra != "" and palabra != " " and palabra != "\n":
            palabras.append(palabra)
            palabra = ""
            
    if palabra != "":
        palabras.append(palabra)
            
    return palabras


def cant_por_linea(linea: str):
    dic: dict = {}

    for palabra in palabras_de_linea(linea):
        if len(palabra) not in dic.keys():
            dic[len(palabra)] = 1
        else:
            dic[len(palabra)] += 1 

    return dic

def prueba(nombre_archivo:str):
    archivo: TextIO = open(nombre_archivo,'r')
    lineas = archivo.readlines()
    list = []
    for linea in lineas:
        list.append(palabras_de_linea(linea))
    return list


def agrupar_por_longitud(nombre_archivo: str) -> dict:
    archivo: TextIO = open(nombre_archivo, 'r')
    lineas: list[str] = archivo.readlines()
    archivo.close()

    dic: dict = {}
    for linea in lineas:
        for palabra in palabras_de_linea(linea):
            if len(palabra) not in dic.keys():
                dic[len(palabra)] = 1
            else:
                dic[len(palabra)] += 1

    return dic

#print(prueba("archivo_con_comentarios.txt"))
#print(agrupar_por_longitud("archivo_con_comentarios.txt"))

'''
  =========================================
  EJERCICIO 21
  =========================================
'''
def la_palabra_mas_frecuenta(nombre_archivo: str) -> str:
    archivo: TextIO = open(nombre_archivo,'r')
    lineas: list[str] = archivo.readlines()

    dic: dict = {}
    for linea in lineas:
        for palabra in palabras_de_linea(linea):
            if palabra not in dic.keys():
                dic[palabra] = 1 
            else:
                dic[palabra] += 1

    

