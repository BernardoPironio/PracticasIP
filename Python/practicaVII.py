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
def es_palindroma(s: list)-> bool:
    state = True
    if len(s) % 2 == 0:
        for i in range(len(s)%2):
            if s[i] != s[-i+1]:
                state = False
    else:
        for i in range(len(s)%2-1):
                    if s[i] != s[-i+1]:
                        state = False

    return state




'''
  =========================================
  EJERCICIO CLASE    
  =========================================
'''

def PalabrasUnidas(ps: list)-> str:
    if ps == []:
        return ''
    oracion: str = ''
    for e in range(len(ps) - 1):
        oracion += ps[e] + ' '
    oracion += ps[len(ps) - 1]
    return oracion

def CeroEnPosicionesPares(s: list)-> list:
    for i in range(len(s)):
        if i%2 == 0:
            s[i] = 0
        else:
            s[i] = s[i]
    return s
        