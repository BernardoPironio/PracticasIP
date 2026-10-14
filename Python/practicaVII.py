'''
  =========================================
  EJERCICIO 1    
  =========================================
'''
# 1
def pertenece(s: list,e: int)-> bool:
    return e in s

# 2
def divide_a_todos(s: list,e: int)-> bool:
    state = True
    for i in range(len(s)):
        if s[i] % e != 0:
            state = False
    return state

# 3
def suma_total(s: list)-> int:
    suma = 0
    for i in s:
        suma += i
    return suma

# 4
def maximo(s: list)-> int:
    max = s[0]
    for i in s:
        if i > max:
            max = i
    return max

# 5
def minimo(s: list)-> int:
    min = s[0]
    for i in s:
        if i < min:
            min = i
    return min

# 6
def ordenados(s: list)-> bool:
    state = True
    for i in range(1,len(s)):
        if s[i - 1] > s[i]:
            state = False
    return state

# 7
def pos_maximo(s: list)-> int:
    if s == []:
        return -1
    for i in range(len(s)):
        if s[i] == maximo(s):
            return i

# 8
def pos_minimo(s: list)-> int:
    if s == []:
        return -1
    for i in range(len(s)):
        if s[i] == minimo(s):
            return i

# 9
def long_mayor_a_siete(s: list)-> bool:
    state = False
    for i in s:
        if len(i) > 7:
            state = True
    return state

# 10
def es_palindroma(s: str) -> bool:
    izquierda = 0
    derecha = len(s) - 1

    while izquierda < derecha:
        if s[izquierda] != s[derecha]:
            return False
        izquierda += 1
        derecha -= 1

    return True

# 11 
def iguales_consecutivos(s: list[int])-> bool:
    tres_iguales: bool = False
    for i in range(len(s)-2):
        if s[i] == s[i+1] and s[i] == s[i+2]:
            tres_iguales = True
    return tres_iguales

# 12
def vocales_distintas(s: str)-> bool:
    vocales: list[int] = ['a','e','i','o','u']
    n: int = 0
    
    for l in s:
        if l in vocales:
            n += 1
            vocales.remove(l)
    state: bool = n >= 3
    return state

# 13
def pos_secuencia_ordenada_mas_larga(s: list[int])-> int:
    max_len = 1
    max_start = 0
    current_len = 1
    current_start = 0

    for i in range(len(s) - 1):
        if s[i] <= s[i+1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_start = current_start
            current_start = i + 1
            current_len = 1
    if current_len > max_len:
        max_len = current_len
        max_start =  current_start
    return max_start 

# 14
def cantidad_digitos_impares(s: list[int])-> int:
    cant: int = 0
    for i in s:
        cant += cant_impares(i)
    return cant

def cant_impares(n: int)-> int:
    cant: int = 0
    while n != 0:
        if (n % 10) % 2 != 0:
            cant += 1
        n = n // 10
    return cant

'''
  =========================================
  EJERCICIO 2
  =========================================
'''
# 1
def CeroEnPosicionesPares(s: list)-> None:
    for i in range(0,len(s),2):
        s[i] = 0

s = [1,2,4,5,6]
CeroEnPosicionesPares(s)
print(s)

# 2
def cero_en_posiciones_pares2 (s: list[int])-> list[int]:
    for i in range(1,len(s),2):
        s[i] = 0
    return s

# 3
def sin_vocales(s: str)-> str:
    vocales: list[str] = ['a','e','i','o','u']
    palabra_sin: str = ''
    for i in s:
        if i not in vocales:
            palabra_sin += i
    return palabra_sin

# 4
def reemplazar_vocales(s: str)-> str:
    vocales: list[str] = ['a','e','i','o','u']
    palabra_reemplazo: str = ''
    for i in range(len(s)):
        if s[i] in vocales:
            palabra_reemplazo += '_'
        else:
            palabra_reemplazo += s[i]
    return palabra_reemplazo

# 5
def da_vuelta_str(s: str)-> str:
    vuelta: str = ''
    for i in range(1,len(s) + 1):
        vuelta += s[len(s) - i]
    return vuelta

# 6
def eliminar_repetidos(s: str)-> str:
    palabra_sin_rep = ''
    for i in s:
        if i not in palabra_sin_rep:
            palabra_sin_rep += i
    return palabra_sin_rep

'''
  =========================================
  EJERCICIO 3
  =========================================
'''
def resultados_materia(s: list[int])-> int:
    valor: int = 3
    if todos_mayor_a(s,4) and promedio(s) >=4:
            valor = 2
    if todos_mayor_a(s,4) and promedio(s) >= 7:
        valor = 1
    return valor

def promedio(s: list[int])-> float:
    suma = 0
    for i in s:
        suma += i
    promedio = suma/len(s)
    return promedio

def todos_mayor_a(s: list[int],n: int)-> bool:
    res: bool = True
    for i in s:
        if i < n:
            res = False
    return res 
'''
  =========================================
  EJERCICIO 4
  =========================================
'''
def saldo_actual(s: list[tuple])-> int:
    saldo: int = 0
    for i in s:
        if i[0] == 'I':
            saldo += i[1]
        if i[0] == 'R':
            saldo -= i[1]
    return saldo

'''
  =========================================
  EJERCICIO 5
  =========================================
'''
# 1
def pertenece_a_cada_uno1(matriz:list[int], e: int, res: list[bool]):
    for pos_fila in range(len(matriz)):
        res[pos_fila] = pertenece(matriz[pos_fila],e)
    return res

# 2
def pertenece_a_cada_uno_version_3(s: list[list[int]], e: int, res: list[bool]) -> None:
  res.clear()  
  for sublista in s:
    res.append(e in sublista)


# 3
def pertenece_a_cada_uno3(matriz: list[int],e: int)-> bool:
    res: list[bool] = []
    for fila in matriz:
        res += [pertenece(fila,e)]
    return res


'''
  =========================================
  EJERCICIO 6
  =========================================
'''
# 1
def es_matriz(m: list[list[int]])-> bool:
    misma_long: bool = True
    for pos_fila in range(len(m) - 1):
        if len(m[pos_fila]) != len(m[pos_fila + 1]):
            misma_long = False 
    return (len(m) > 0 and len(m[0]) > 0) and misma_long

# 2

'''
  =========================================
  EJERCICIO CLASE     
  =========================================
'''
# Palabras undidas
def PalabrasUnidas(ps: list)-> str:
    if ps == []:
        return ''
    oracion: str = ''
    for e in range(len(ps) - 1):
        oracion += ps[e] + ' '
    oracion += ps[len(ps) - 1]
    return oracion

# Sumar toda la matriz
def sumar_toda_la_matriz(matriz: list[list[int]])-> int:
    suma = 0
    for columna in matriz:
        for i in columna:
            suma += i
    return suma

# Columna
def columna(matriz: list[list[int]],col: int)-> list[int]:
    columna = []
    for i in matriz:
        columna.append(i[col])
    return columna

# Columnas ordenadas
def columnas_ordenadas(matriz: list[list[int]])-> list[bool]:
    res = []
    for col in range(len(matriz)):
        res += [ordenados(columna(matriz,col))]
    return res

