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
    maximo: int = cola_aux.get()
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
# 1
pila1 = Pila()
pila1.put("linkedin")
pila1.put("github")
pila1.put("gitlab")

pila2 = Pila()
pila2.put("dm")
pila2.put("df")
pila2.put("dc")

historiales = {"bpiro":pila1,"lu": pila2}

# 2
def visitar_sitio(historiales: dict[str,Pila[str]],usuario: str,sitio: str) -> None:
    if usuario in historiales.keys():
        historiales[usuario].put(sitio)
    elif usuario not in historiales.keys():
        pila_aux = Pila()
        pila_aux.put(sitio)
        historiales[usuario] = pila_aux

# 3
def navegar_atras(historiales: dict[str,Pila[str]],usuario: str) -> str:
    return historiales[usuario].get()

'''
  =========================================
  EJERCICIO 18
  =========================================
'''
inventario: dict[str,dict[str,float|int]] =  {'remera': {'precio': 999.99, 'cantidad': 3}}

# 1
def agregar_producto(inventario: dict[str,dict[str,float|int]], nombre: str, precio: float, cantidad:int) -> None:
    inventario[nombre] = {'precio': precio,'cantidad':cantidad}

# 2
def actualizar_stock(inventario: dict[str,dict[str,float|int]], nombre:str, cantidad: int) -> None:
    inventario[nombre]['cantidad'] = cantidad

# 3
def actualizar_precio(inventario: dict[str,dict[str,float|int]], nombre:str, precio: int) -> None:
    inventario[nombre]['precio'] = precio

# 4
def calcular_valor_inventario(inventario: dict[str,dict[str,float|int]]) -> float:
    suma: float = 0

    for nombre in inventario.keys():
        suma += inventario[nombre]['precio']*inventario[nombre]['cantidad']

    return suma

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

# 2
def existe_palbra(nombre_archivo: str, palabra: str) -> bool:
    archivo: TextIO = open(nombre_archivo,'r')
    lineas: list[str] = archivo.readlines()
    archivo.close()
    res: bool = False
    for linea in lineas:
        if palabra in linea:
            res = True
    return res

# 3
def separar_palabras(oracion: str) -> list[str]:
    palabras: list[str] = []
    i: int = 0
    n: int = len(oracion)
    
    while i < n:
        while i < n and oracion[i] == ' ':
            i += 1
            
        if i < n:
            palabra_actual: str = ""
            
            while i < n and oracion[i] != ' ':
                palabra_actual += oracion[i]
                i += 1
                
            palabras.append(palabra_actual)
            
    return palabras

def cantidad_de_apariciones(nombre_archivo: str, palabra: str) -> int:
    archivo: TextIO = open(nombre_archivo,'r')
    lineas: list[str] = archivo.readlines()
    archivo.close()
    contador: int = 0

    for linea in lineas:
        for e in separar_palabras(linea):
            if e == palabra:
                contador += 1

    return contador

'''
  =========================================
  EJERCICIO 20
  =========================================
'''
def agrupar_por_longitud(nombre_archivo: str) -> dict[int,int]:
    archivo: TextIO = open(nombre_archivo,'r')
    lineas: list[str] = archivo.readlines()
    archivo.close()

    res: dict[int,int] = {}

    for linea in lineas:
        for palabra in separar_palabras(linea):
            if len(palabra) not in res.keys():
                res[len(palabra)] = 1
            else:
                res[len(palabra)] += 1

    return res

'''
  =========================================
  EJERCICIO 21
  =========================================
'''
def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    archivo: TextIO = open(nombre_archivo,'r')
    lineas: list[str] = archivo.readlines()
    archivo.close()
    cantidad_palabras: dict[str,int] = {}

    for linea in lineas:
        for palabra in separar_palabras(linea):
            if palabra not in cantidad_palabras.keys():
                cantidad_palabras[palabra] = 1
            else:
                cantidad_palabras[palabra] += 1

    
        
    return cantidad_palabras

'''
  =========================================
  EJERCICIO 22
  =========================================
'''
def clonar_sin_comentarios(nombre_archivo_entrada, nombre_archivo_salida):
    entrada = open(nombre_archivo_entrada)
    salida = open(nombre_archivo_salida, 'w')
    
    for linea in entrada:
        es_comentario = False
        i = 0
        while i < len(linea) and linea[i] == ' ':
            i = i + 1
            
        if i < len(linea) and linea[i] == '#':
            es_comentario = True
            
        if not es_comentario:
            salida.write(linea)
            
    entrada.close()
    salida.close()

'''
  =========================================
  EJERCICIO 23
  =========================================
'''
def invertir_lineas(nombre_archivo_entrada, nombre_archivo_salida):
    entrada = open(nombre_archivo_entrada)
    salida = open(nombre_archivo_salida, 'w')
    
    lineas = []
    for linea in entrada:
        lineas = lineas + [linea]
        
    i = len(lineas) - 1
    while i >= 0:
        salida.write(lineas[i])
        i = i - 1
        
    entrada.close()
    salida.close()

'''
  =========================================
  EJERCICIO 24
  =========================================
'''
def agregar_frase_al_final(nombre_archivo, frase):
    archivo = open(nombre_archivo, 'a')
    archivo.write(frase + '\n')
    archivo.close()

'''
  =========================================
  EJERCICIO 25
  =========================================
'''
def agregar_frase_al_principio(nombre_archivo, frase):
    archivo = open(nombre_archivo)
    lineas = []
    for linea in archivo:
        lineas = lineas + [linea]
    archivo.close()
    
    archivo = open(nombre_archivo, 'w')
    archivo.write(frase + '\n')
    
    i = 0
    while i < len(lineas):
        archivo.write(lineas[i])
        i = i + 1
        
    archivo.close()

'''
  =========================================
  EJERCICIO 26
  =========================================
'''
def listar_textos_de_archivo(nombre_archivo):
    archivo = open(nombre_archivo, 'rb')
    contenido = archivo.read()
    archivo.close()
    
    textos = []
    texto_actual = ""
    
    i = 0
    while i < len(contenido):
        b = contenido[i]
        c = chr(b)
        
        es_legible = (
            (c >= '0' and c <= '9') or
            (c >= 'A' and c <= 'Z') or
            (c >= 'a' and c <= 'z') or
            c == ' ' or
            c == '_'
        )
        
        if es_legible:
            texto_actual = texto_actual + c
        else:
            if len(texto_actual) >= 5:
                textos = textos + [texto_actual]
            texto_actual = ""
            
        i = i + 1
        
    if len(texto_actual) >= 5:
        textos = textos + [texto_actual]
        
    return textos

'''
  =========================================
  EJERCICIO 27
  =========================================
'''
def promedio_estudiante(notas_de_estudiantes, lu):
    suma = 0.0
    cantidad = 0
    
    i = 0
    while i < len(notas_de_estudiantes):
        linea = notas_de_estudiantes[i]
        if linea.endswith('\n'):
            linea = linea[:-1]
            
        if len(linea) > 0:
            partes = []
            parte_actual = ""
            j = 0
            while j < len(linea):
                if linea[j] == ',':
                    partes = partes + [parte_actual]
                    parte_actual = ""
                else:
                    parte_actual = parte_actual + linea[j]
                j = j + 1
            partes = partes + [parte_actual]
            
            if len(partes) >= 4 and partes[0] == lu:
                nota = float(partes[3])
                suma = suma + nota
                cantidad = cantidad + 1
                
        i = i + 1
        
    return suma / cantidad


def calcular_promedio_por_estudiante(nombre_archivo_notas, nombre_archivo_promedios):
    archivo_notas = open(nombre_archivo_notas)
    notas_de_estudiantes = []
    for linea in archivo_notas:
        notas_de_estudiantes = notas_de_estudiantes + [linea]
    archivo_notas.close()
    
    lus_procesadas = []
    i = 0
    while i < len(notas_de_estudiantes):
        linea = notas_de_estudiantes[i]
        if linea.endswith('\n'):
            linea = linea[:-1]
            
        if len(linea) > 0:
            partes = []
            parte_actual = ""
            j = 0
            while j < len(linea):
                if linea[j] == ',':
                    partes = partes + [parte_actual]
                    parte_actual = ""
                else:
                    parte_actual = parte_actual + linea[j]
                j = j + 1
            partes = partes + [parte_actual]
            
            if len(partes) >= 4:
                lu = partes[0]
                ya_esta = False
                k = 0
                while k < len(lus_procesadas):
                    if lus_procesadas[k] == lu:
                        ya_esta = True
                    k = k + 1
                if not ya_esta:
                    lus_procesadas = lus_procesadas + [lu]
                    
        i = i + 1
        
    archivo_promedios = open(nombre_archivo_promedios, 'w')
    
    i = 0
    while i < len(lus_procesadas):
        lu = lus_procesadas[i]
        prom = promedio_estudiante(notas_de_estudiantes, lu)
        archivo_promedios.write(lu + ',' + str(prom) + '\n')
        i = i + 1
        
    archivo_promedios.close()