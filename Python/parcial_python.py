from queue import LifoQueue as Pila

# Ejercicio 1

def ejercicio1(s: list[int], objetivo: int) -> tuple[int, int]:

	largo: int = len(s)

	for i in range(len(s)):
		contador: int = 1
		
		while i + contador < len(s):
			if s[i] + s[i + contador] == objetivo and contador < largo:
				res: tuple = (i,i + contador)
				largo = contador

			contador += 1

	return res

# Ejercicio 4

def separar_pedidos_express(pedidos: Pila[tuple[int, bool]]) -> Pila[int]:
	res: Pila[int] = Pila()
	res_invertido: Pila[int] = Pila()
	pedidos_invertido: Pila[int] = Pila()

	while not pedidos.empty():
		elemento = pedidos.get()

		if elemento[1]:
			res_invertido.put(elemento[0])
		else:
			pedidos_invertido.put(elemento)

	while not res_invertido.empty():
		elemento = res_invertido.get()
		res.put(elemento)

	while not pedidos_invertido.empty():
		elemento = pedidos_invertido.get()
		pedidos.put(elemento)

	return res

# Ejercicio 5

def ejercicio5(A: list[list[int]]) -> None:
	maximo: int = A[0][0]
	fila_maximo: int = 0
	
	for f in range(len(A)):
		for c in range(len(A[0])):
			if A[f][c] > maximo:
				maximo = A[f][c]
				fila_maximo = f

	for c in range(len(A[0])):
		A[fila_maximo][c] = 2 * A[fila_maximo][c]


# Ejercicio 7

def estudiantes_destacados_por_cantidad_de_cursos(calificaciones: dict[str, list[int]], nota_minima: int) -> dict[int, list[str]]:
	res: dict[int,list[str]] = {}

	for estudiante in calificaciones.keys():
		destacado: bool = True

		for nota in calificaciones[estudiante]:
			destacado = destacado and (nota >= nota_minima)

		if destacado:
			if len(calificaciones[estudiante]) not in res.keys():
				res[len(calificaciones[estudiante])] = [estudiante]
			else:
				res[len(calificaciones[estudiante])].append(estudiante)
	
	return res
		
