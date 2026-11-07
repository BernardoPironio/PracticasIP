'''
  =========================================
  EJERCICIO 1    
  =========================================
'''
def productos_en_stock(stock_cambios: list[tuple[str,int]]) -> dict[str,tuple[int,int]]:
    res: dict[str,tuple[int,int]] = {}

    for cambio in stock_cambios:

        if cambio[0] not in res.keys():
            res[cambio[0]] = (cambio[1],cambio[1])
        else:
            if cambio[1] < res[cambio[0]][0]:
                res[cambio[0]] = (cambio[1],res[cambio[0]][1])
            elif cambio[1] > res[cambio[0]][1]:
                res[cambio[0]] = (res[cambio[0]][0],cambio[1])

    return res

'''
  =========================================
  EJERCICIO 2
  =========================================
'''
def es_primo(n: int) -> bool:
    res: bool = n >= 2  
    div: int = 2
    
    while res and (div * div <= n):
        if n % div == 0:
            res = False
        div += 1
        
    return res

def filtrar_codigos_primos(codigos_barra: list[int]) -> list[int]:
    codigos_primos: list[int] = []

    for codigo in codigos_barra:
        ultimos_tres = codigo % 1000

        if es_primo(ultimos_tres):
            codigos_primos.append(codigo)
    
    return codigos_primos

'''
  =========================================
  EJERCICIO 3
  =========================================
'''
def subsecuencia_mas_larga(tipos_pacientes_atendidos: list[str]) -> int:
    indice_max: int = -1
    maximo: int = 0

    for i in range(len(tipos_pacientes_atendidos)):
        cant_actual: int = 0
        contador: int = 0

        while i + contador < len(tipos_pacientes_atendidos) and tipos_pacientes_atendidos[i + contador] in ["perro","gato"]:
            cant_actual += 1
            contador += 1

        if cant_actual > maximo:
            indice_max = i
            maximo = cant_actual

    return indice_max

'''
  =========================================
  EJERCICIO 4
  =========================================
'''
def un_responsable_por_turno(grilla_horaria: list[list[str]]) -> list[tuple[bool,bool]]:
    res: list[tuple[bool,bool]] = []

    for dia in range(len(grilla_horaria[0])):

        bool_mañana: bool = grilla_horaria[0][dia] == grilla_horaria[1][dia]
        for i in range(3):
            bool_mañana = bool_mañana and grilla_horaria[i][dia] == grilla_horaria[i + 1][dia]

        bool_tarde: bool = grilla_horaria[4][dia] == grilla_horaria[5][dia]
        for i in range(4,7):
            bool_tarde = bool_tarde and grilla_horaria[i][dia] == grilla_horaria[i + 1][dia]

        res.append((bool_mañana,bool_tarde))

    return res

'''
  =========================================
  EJERCICIO 5
  =========================================
'''
def promedio_lista(lista:list[int]) -> float:
    promedio: int = 0
    for e in lista:
        promedio += e
    return promedio/len(lista)

def promedio_de_salidas(registro: dict[str,list[int]]) -> dict[str,tuple[int,float]]:
    res: dict[str,tuple[int,float]] = {}

    for integrante in registro.keys():
        contador: int = 0
        lista_terminados: list[int] = []

        for tiempo in registro[integrante]:
            if 0 < tiempo < 61:
                lista_terminados.append(tiempo)
                contador += 1
            if lista_terminados != []:
                promedio: float = promedio_lista(lista_terminados)
            else: 
                promedio = float(0)

        res[integrante] = (contador,promedio)

    return res

'''
  =========================================
  EJERCICIO 6
  =========================================
'''

