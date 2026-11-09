from queue import Queue as Cola
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
def tiempo_mas_rapido(tiempos_salas: list[int]) -> int:
    mas_rapido: int = 61

    for i in range(len(tiempos_salas)):
        if tiempos_salas[i] < mas_rapido and tiempos_salas[i] != 0:
            mas_rapido = tiempos_salas[i]
            mas_rapido_indice: int = i

    return mas_rapido_indice
    
'''
  =========================================
  EJERCICIO 7
  =========================================
'''
def racha_mas_larga(tiempos: list[int]) -> tuple[int,int]:
    cantidad_max: int = 0
    indicie_inicial: int = 0

    for i in range(len(tiempos)):
        contador: int = 0

        while i + contador < len(tiempos) and 0 < tiempos[i+contador] < 61:
            contador += 1

        if contador > cantidad_max:
            cantidad_max = contador 
            indicie_inicial = i

    return (indicie_inicial,indicie_inicial + cantidad_max - 1)

'''
  =========================================
  EJERCICIO 8
  =========================================
'''
def escape_en_solitario(amigos_por_sala: list[list[int]]) -> list[int]:
    res: list[int] = []

    for sala in amigos_por_sala:
        if sala[0] == sala[1] == sala[3] == 0 and sala[2] != 0:
            res.append(amigos_por_sala.index(sala))

    return res

'''
  =========================================
  EJERCICIO 9
  =========================================
'''
def torneo_de_gallinas(estrategias: dict[str,str]) -> dict[str,int]:
    jugadores: list[str] = list(estrategias.keys())
    res: dict[str,int] = {}

    for jugador in jugadores:
        jugada: str = estrategias[jugador]
        puntos: int = 0

        for otro in jugadores:

             if jugada == "me desvío siempre" and jugada == estrategias[otro]:
                 puntos -= 10 

             elif jugada == "me desvío siempre":
                 puntos -= 15

             elif jugada == "me la banco y no me desvío" and jugada == estrategias[otro]:
                 puntos -= 5

             elif jugada == "me la banco y no me desvío":
                 puntos += 10

        if jugada == "me desvío siempre":
            puntos += 10
        else:
            puntos += 5
        
        res[jugador] = puntos

    return res
   
'''
  =========================================
  EJERCICIO 10
  =========================================
'''
def reordenar_cola_priorizando_vips(fila_clientes: Cola[tuple[str,str]]) -> Cola[str]:
    cola_aux: Cola[tuple[str,str]] = Cola()
    cola_no_vips: Cola[str] = Cola()
    res: Cola[str] = Cola()

    while not fila_clientes.empty():
        elemento = fila_clientes.get()
        cola_aux.put(elemento)

        if elemento[1] == "vip":
            res.put(elemento[0])
        else: 
            cola_no_vips.put(elemento[0])

    while not cola_no_vips.empty():
        res.put(cola_no_vips.get())

    while not cola_aux.empty():
        fila_clientes.put(cola_aux.get())
        
    return res

'''
  =========================================
  EJERCICIO 11
  =========================================
'''
def es_palindormo(palabra: str) -> bool:
    res: bool = True
    
    for letra in range(len(palabra)//2): 
        una: str = palabra[letra]
        otra: str = palabra[len(palabra) - 1 - letra] 
        iguales: bool =  una == otra
        res = res and iguales

    return res

def texto_desde(texto: str,desde:int) -> str:
    res: str = ''

    for i in range(desde,len(texto)):
        res += texto[i]

    return res

def cuantos_sufijos_son_palindromos(texto: str) -> int:
    contador: int = 0

    for i in range(len(texto)):
        if es_palindormo(texto_desde(texto,i)):
            contador += 1

    return contador

'''
  =========================================
  EJERCICIO 12
  =========================================
'''
def quien_gano_el_tateti_facilito(tablero: list[list[str]]) -> int:
    gano_x: bool = False
    gano_o: bool = False

    for f in range(len(tablero) - 2):
        for c in range(len(tablero)):
            if tablero[f][c] == "X" and tablero[f + 1][c] == "X" and tablero[f + 2][c] == "X":
                gano_x = True

            if tablero[f][c] == "O" and tablero[f + 1][c] == "O" and tablero[f + 2][c] == "O":
                gano_o = True

    res: int = 0

    if gano_x and gano_o:
        res = 3
    elif gano_o:
        res = 2
    elif gano_x:
        res = 1

    return res

'''
  =========================================
  EJERCICIO 13
  =========================================
'''
def orden_de_atencion(urgentes: Cola[int],postergables: Cola[int]) -> Cola[int]:
    urgentes_aux: Cola[int] = Cola()
    postergables_aux: Cola[int] = Cola()
    res: Cola[int] = Cola()

    while not urgentes.empty():
        urgente = urgentes.get()
        urgentes_aux.put(urgente)
        res.put(urgente)

        postergable = postergables.get()
        postergables_aux.put(postergable)
        res.put(postergable)

    while not urgentes_aux.empty():
        urgente = urgentes_aux.get()
        urgentes.put(urgente)

        postergable = postergables_aux.get()
        postergables.put(postergable)

    return res

'''
  =========================================
  EJERCICIO 14
  =========================================
'''
def alarma_epidemiologica(registros: list[tuple[int,str]], infecciosas: list[str], umbral: float) -> dict[str,float]:
    res: dict[str,float] = {}

    for enfermedad in infecciosas:
        cantidad: int = 0

        for registro in registros:
            if registro[1] == enfermedad:
                cantidad += 1

        porcentaje: int = cantidad/len(registros)

        if porcentaje >= umbral:
            res[enfermedad] = porcentaje

    return res

'''
  =========================================
  EJERCICIO 15
  =========================================
'''