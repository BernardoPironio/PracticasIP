from typing import TextIO
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

    

