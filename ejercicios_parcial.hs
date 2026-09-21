import Test.HUnit
{-
  =========================================
  EJERCICIO 1
  =========================================
-}

generarStock:: [String] -> [(String, Integer)]
generarStock []     = []
generarStock (x:xs) = [(x,cantidad x (x:xs))] ++ generarStock (eliminarTodos x (x:xs))

cantidad:: String -> [String] -> Integer
cantidad _ [] = 0
cantidad s (x:xs) | x == s    = 1 + cantidad s xs
                  | otherwise = cantidad s xs

pertenece::(Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece n (x:xs)  | n == x    = True
                    | otherwise = pertenece n xs

eliminarTodos::(Eq t) => t -> [t] -> [t]
eliminarTodos _ [] = []
eliminarTodos e (x:xs)  | e == x    = eliminarTodos e xs
                        | otherwise = x : eliminarTodos e xs

{-
  =========================================
  EJERCICIO 2
  =========================================
-}

stockDeProducto:: [(String, Integer)] -> String -> Integer
stockDeProducto [] _ = 0
stockDeProducto (x:xs) producto | inStock x producto = cantidadStock x
                                | otherwise          = stockDeProducto xs producto

cantidadStock:: (String,Integer) -> Integer
cantidadStock (_,y) = y

inStock:: (String,Integer) -> String -> Bool
inStock (x,_) z | x == z    = True
                | otherwise = False

{-
  =========================================
  EJERCICIO 3
  =========================================
-}

dineroEnStock:: [(String, Integer)] -> [(String, Float)] -> Float
dineroEnStock [] _          = 0
dineroEnStock (y:ys) (x:xs) = precioDeProducto (fst y) (x:xs) * fromIntegral (snd y) + dineroEnStock ys (x:xs)

precioDeProducto:: String -> [(String, Float)] -> Float
precioDeProducto producto (x:xs)  | producto == fst x = snd x
                                  | otherwise         = precioDeProducto producto xs

{-
  =========================================
  EJERCICIO 4
  =========================================
-}

aplicarOferta :: [(String, Integer)] ->[(String, Float)] ->[(String,Float)]
aplicarOferta [] _ = []
aplicarOferta (y:ys) (x:xs) | stockDeProducto (y:ys) (fst y) > 10 = [(fst y,0.8*precioDeProducto (fst y) (x:xs))] ++ aplicarOferta ys (x:xs)
                            | otherwise                           = [(fst y,precioDeProducto (fst y) (x:xs))] ++ aplicarOferta ys (x:xs)

{-
  =========================================
  EJERCICIO 5
  =========================================
-}

type Fila     = [Integer]
type Tablero  = [Fila]
type Posicion = (Integer,Integer)
type Camino   = [Posicion]

tablero = [[13,12,6,4],[1,1,32,25],[9,2,14,7],[7,3,5,16],[27,2,8,18]]

maximo:: Tablero -> Integer
maximo (fila:resto) = maximoFila (listaMaximos (fila:resto))

maximoFila:: Fila -> Integer
maximoFila [x] = x
maximoFila (elemento:resto)  | elemento >= maximoFila resto = elemento
                             | otherwise                    = maximoFila resto

listaMaximos:: Tablero -> [Integer]
listaMaximos []     = []
listaMaximos (x:xs) = [maximoFila x] ++ listaMaximos xs

{-
  =========================================
  EJERCICIO 6
  =========================================
-}

masRepetido:: Tablero -> Integer
masRepetido (x:xs) = masRepetidoFila (aplanar (x:xs))

masRepetidoFila :: Fila -> Integer
masRepetidoFila [x] = x
masRepetidoFila (x:xs)  | cantElementos x (x:xs) >= cantElementos (masRepetidoFila xs) (x:xs) = x
                        | otherwise                                                           = masRepetidoFila xs

cantElementos:: Integer -> Fila -> Integer
cantElementos _ [] = 0
cantElementos e (x:xs)  | e == x    = 1 + cantElementos e xs
                        | otherwise = cantElementos e xs

aplanar:: Tablero -> [Integer]
aplanar []           = []
aplanar (fila:resto) = fila ++ aplanar resto

{-
  =========================================
  EJERCICIO 7
  =========================================
-}

valoresDeCamino:: Tablero -> Camino -> [Integer]
valoresDeCamino _ []                      = []
valoresDeCamino tablero (posicion:camino) = [elementoFila (elementoTablero tablero (fst posicion)) (snd posicion)] ++ valoresDeCamino tablero camino

elementoFila:: Fila -> Integer -> Integer
elementoFila [x] _ = x
elementoFila (x:xs) e | e - 1 == 0 = x 
                      | otherwise  = elementoFila xs (e - 1)

elementoTablero:: Tablero -> Integer -> Fila
elementoTablero [x] _ = x
elementoTablero (x:xs) e | e - 1 == 0 = x
                      | otherwise     = elementoTablero xs (e - 1)

{-
  =========================================
  EJERCICIO 8
  =========================================
-}

esCaminoFibo:: [Integer] -> Integer -> Bool
esCaminoFibo [] _ = True
esCaminoFibo (x:xs) e = x == fib e && esCaminoFibo xs (e + 1)

fib:: Integer -> Integer
fib n | n == 0    = 0
      | n == 1    = 1
      | otherwise = fib (n - 1) + fib (n - 2)

{-
  =========================================
  EJERCICIO 9
  =========================================
-}

divisoresPropios:: Integer -> [Integer]
divisoresPropios n = esDivisorPropio n 1 

esDivisorPropio:: Integer -> Integer -> [Integer]
esDivisorPropio n k | k == (div n 2 + 1) = []
                    | mod n k == 0       = [k] ++ esDivisorPropio n (k+1)
                    | otherwise          = esDivisorPropio n (k + 1)

{-
  =========================================
  EJERCICIO 10
  =========================================
-}

sonAmigos:: Integer -> Integer -> Bool
sonAmigos n m = sumarElementos (divisoresPropios n) == m && sumarElementos (divisoresPropios m) == n

sumarElementos:: [Integer] -> Integer
sumarElementos []     = 0
sumarElementos (x:xs) = x + sumarElementos xs

{-
  =========================================
  EJERCICIO 11
  =========================================
-}

losPrimerosNPerfectos:: Integer -> [Integer]
losPrimerosNPerfectos n =  listaDePerfectos n 1

esPerfecto:: Integer -> Bool
esPerfecto n = n == sumarElementos (divisoresPropios n)

listaDePerfectos:: Integer -> Integer -> [Integer]
listaDePerfectos n k  | n == 0       = []
                      | esPerfecto k = [k] ++ listaDePerfectos (n - 1) (k + 1)
                      | otherwise    = listaDePerfectos n (k + 1)

{-
  =========================================
  EJERCICIO 12
  =========================================
-}

listaDeAmigos:: [Integer] -> [(Integer,Integer)]
listaDeAmigos [] = []
listaDeAmigos (x:xs)  | pertenece (sumarElementos (divisoresPropios x)) xs = [(x, sumarElementos (divisoresPropios x))] ++ listaDeAmigos xs
                      | otherwise = listaDeAmigos xs

{-
  =========================================
  TESTS
  =========================================
-}

-- ejercicio 1
test1:: Test
test1 = test [
  "Lista vacia" ~: (generarStock []) ~?= [],
  "3 manzanas, 2 peras" ~: (generarStock ["manzana","pera","manzana","pera","manzana"]) ~?= [("manzana",3),("pera",2)],
  "1 1 y 1" ~: (generarStock ["manzana","pera","banana"]) ~?= [("manzana",1),("pera",1),("banana",1)],
  "Lista vacia" ~: (generarStock []) ~?= [],
  "Un solo producto repetido varias veces" ~: (generarStock ["arroz", "arroz", "arroz"]) ~?= [("arroz", 3)],
  "Un solo elemento en la lista" ~: (generarStock ["leche"]) ~?= [("leche", 1)],
  "Todos los productos distintos" ~: (generarStock ["manzana", "pera", "banana"]) ~?= [("manzana", 1), ("pera", 1), ("banana", 1)],
  "Productos en bloques seguidos" ~: (generarStock ["pan", "pan", "queso", "queso", "queso"]) ~?= [("pan", 2), ("queso", 3)],
  "Productos intercalados" ~: (generarStock ["manzana", "pera", "manzana", "pera", "manzana"]) ~?= [("manzana", 3), ("pera", 2)],
  "Cadenas vacias como producto" ~: (generarStock ["", "", "pan"]) ~?= [("", 2), ("pan", 1)]
  ]

-- ejercicio 2
test2:: Test
test2 = test [
  "Inicial" ~: (stockDeProducto [("manzana",3),("banana",2),("salmon", 122)] "salmon") ~?= 122,
  "Vacio" ~: (stockDeProducto [] "salmon") ~?= 0,
  "Inicial" ~: (stockDeProducto [("manzana",1),("banana",1),("salmon", 1)] "manzana") ~?= 1,
  "Inicial" ~: (stockDeProducto [("manzana",3),("banana",2)] "salmon") ~?= 0,
  "Stock vacio" ~: (stockDeProducto [] "manzana") ~?= 0,
  "Producto existe al principio" ~: (stockDeProducto [("manzana", 3), ("pera", 2)] "manzana") ~?= 3,
  "Producto existe en el medio" ~: (stockDeProducto [("manzana", 3), ("pera", 5), ("banana", 1)] "pera") ~?= 5,
  "Producto existe al final" ~: (stockDeProducto [("manzana", 3), ("pera", 2), ("banana", 4)] "banana") ~?= 4,
  "Producto NO existe en el stock" ~: (stockDeProducto [("manzana", 3), ("pera", 2)] "frutilla") ~?= 0,
  "Unico elemento que coincide" ~: (stockDeProducto [("leche", 10)] "leche") ~?= 10,
  "Unico elemento que NO coincide" ~: (stockDeProducto [("leche", 10)] "pan") ~?= 0
  ]

-- ejercicio 3
test3:: Test
test3 = test [
  "Inicial" ~: (dineroEnStock [("manzana",3),("pera",2),("tomate",4)] [("manzana",10),("pera",15),("tomate",5)]) ~?= 80,
  "Sin stock" ~: (dineroEnStock [] [("manzana",10),("pera",15),("tomate",5)]) ~?= 0,
  "Stock vacio" ~: (dineroEnStock [] [("manzana", 10.0), ("pera", 15.0)]) ~?= 0.0,
  "Un solo producto en stock" ~: (dineroEnStock [("manzana", 3)] [("manzana", 10.5)]) ~?= 31.5,
  "Varios productos en stock (precios en el mismo orden)" ~: (dineroEnStock [("manzana", 2), ("pera", 4)] [("manzana", 10.0), ("pera", 5.0)]) ~?= 40.0,
  "Varios productos en stock (precios desordenados respecto al stock)" ~: (dineroEnStock [("manzana", 3), ("pera", 2), ("tomate", 4)] [("tomate", 5.0), ("pera", 15.0), ("manzana", 10.0)]) ~?= 80.0,
  "Lista de precios tiene productos de mas que no estan en stock" ~: (dineroEnStock [("pera", 2)] [("manzana", 10.0), ("pera", 15.5), ("banana", 8.0)]) ~?= 31.0,
  "Multiplicacion con decimales" ~: (dineroEnStock [("leche", 3)] [("leche", 2.5)]) ~?= 7.5
  ]

-- ejercicio 4
test4:: Test
test4 = test [
  "Inicial" ~: (aplicarOferta [("manzana",3),("pera",2),("tomate",11)] [("manzana",10),("pera",15),("tomate",5)]) ~?= [("manzana",10),("pera",15),("tomate",4)],
  "Stock vacio" ~: (aplicarOferta [] [("manzana", 10.0), ("pera", 15.0)]) ~?= [],
  "Un solo producto en stock" ~: (aplicarOferta [("manzana", 12)] [("manzana", 10)]) ~?= [("manzana", 8)],
  "Un solo producto en stock <10" ~: (aplicarOferta [("manzana", 7)] [("manzana", 10)]) ~?= [("manzana", 10)],
  "Precios vacio" ~: (aplicarOferta [] []) ~?= [],
  "Producto con stock mayor a 10 (se aplica oferta 20% de descuento)" ~: (aplicarOferta [("manzana", 11)] [("manzana", 100.0)]) ~?= [("manzana", 80.0)],
  "Producto con stock exactamente igual a 10 (caso limite: NO se aplica oferta)" ~: (aplicarOferta [("pera", 10)] [("pera", 50.0)]) ~?= [("pera", 50.0)],
  "Producto con stock menor a 10 (NO se aplica oferta)" ~: (aplicarOferta [("banana", 5)] [("banana", 40.0)]) ~?= [("banana", 40.0)]
  ]

-- ejercicio 5
test5:: Test
test5 = test [
  "Tablero minimo de 1x1" ~: (maximo [[5]]) ~?= 5,
  "Tablero de 1 fila y varias columnas" ~: (maximo [[3, 8, 2, 5]]) ~?= 8,
  "Tablero de varias filas y 1 columna" ~: (maximo [[4], [10], [1]]) ~?= 10,
  "Maximo esta al principio del tablero (0,0)" ~: (maximo [[100, 20], [5, 10]]) ~?= 100,
  "Maximo esta al final del tablero" ~: (maximo [[1, 2], [3, 99]]) ~?= 99,
  "Maximo esta en el medio del tablero" ~: (maximo [[1, 2, 3], [4, 50, 6], [7, 8, 9]]) ~?= 50,
  "Todos los elementos del tablero son iguales" ~: (maximo [[7, 7], [7, 7]]) ~?= 7,
  "Maximo repetido en varias posiciones" ~: (maximo [[15, 2], [3, 15]]) ~?= 15
  ]

-- ejercicio 6
test6:: Test
test6 = test [
  "Tablero minimo de 1x1" ~: (masRepetido [[5]]) ~?= 5,
  "Un numero claramente mas repetido que el resto" ~: (masRepetido [[1, 2, 2], [3, 2, 4], [2, 5, 2]]) ~?= 2,
  "Tablero donde todos los numeros son iguales" ~: (masRepetido [[7, 7], [7, 7]]) ~?= 7,
  "Ningun numero se repite (todos aparecen 1 vez)" ~: (masRepetido [[1, 2], [3, 4]]) ~?= 1,  -- Valido devolver 1, 2, 3 o 4 por desempate
  "Empate de frecuencia entre dos numeros" ~: (masRepetido [[1, 1, 2], [2, 3, 4]]) ~?= 1,  -- Valido devolver 1 o 2 (ambos aparecen 2 veces)
  "Tablero de 1 fila y varias columnas" ~: (masRepetido [[4, 8, 8, 5]]) ~?= 8,
  "Tablero de varias filas y 1 columna" ~: (masRepetido [[3], [3], [10]]) ~?= 3
  ]

-- ejercicio 7
test7:: Test
test7 = test [
  "Camino verde de la imagen" ~: (valoresDeCamino tablero [(2,1), (2,2), (3,2), (4,2), (4,3)]) ~?= [1, 1, 2, 3, 5],
  "Camino por la primera fila (horizontal)" ~: (valoresDeCamino tablero [(1,1), (1,2), (1,3), (1,4)]) ~?= [13, 12, 6, 4],
  "Camino por la primera columna (vertical)" ~: (valoresDeCamino tablero [(1,1), (2,1), (3,1), (4,1), (5,1)]) ~?= [13, 1, 9, 7, 27],
  "Una sola casilla del tablero" ~: (valoresDeCamino tablero [(3,3)]) ~?= [14],
  "Camino vacio" ~: (valoresDeCamino [[1, 2], [3, 4]] []) ~?= [],
  "Camino con una sola posicion" ~: (valoresDeCamino [[5, 6], [7, 8]] [(1, 1)]) ~?= [5],
  "Camino horizontal (solo desplazamientos hacia la derecha)" ~: (valoresDeCamino [[10, 20, 30]] [(1, 1), (1, 2), (1, 3)]) ~?= [10, 20, 30],
  "Camino vertical (solo desplazamientos hacia abajo)" ~: (valoresDeCamino [[100], [200], [300]] [(1, 1), (2, 1), (3, 1)]) ~?= [100, 200, 300],
  "Camino mixto (derecha y abajo)" ~: (valoresDeCamino [[1, 2, 3], [4, 5, 6], [7, 8, 9]] [(1, 1), (1, 2), (2, 2), (3, 2), (3, 3)]) ~?= [1, 2, 5, 8, 9],
  "Camino que repite posiciones o recorre valores duplicados" ~: (valoresDeCamino [[4, 4], [4, 4]] [(1, 1), (1, 2), (2, 2)]) ~?= [4, 4, 4]
  ]

-- ejercicio 8
test8:: Test
test8 = test [
  "Caso ejemplo enunciado" ~:(esCaminoFibo [1,1,2,3,5] 1) ~?= True,
  "Caso un elemento, coincide" ~:(esCaminoFibo [1] 1) ~?= True,
  "Caso un elemento, no coincide" ~:(esCaminoFibo [2] 1) ~?= False,
  "Caso i = 0, nunca puede matchear (f(0)=0 y s es positiva)" ~:(esCaminoFibo [1] 0) ~?= False,
  "Caso tramo intermedio de la sucesion" ~:(esCaminoFibo [5,8,13] 5) ~?= True,
  "Caso valores correctos pero desordenados" ~:(esCaminoFibo [1,2,1,3,5] 1) ~?= False,
  "Caso un valor incorrecto en el medio" ~:(esCaminoFibo [1,1,2,4,5] 1) ~?= False,
  "Caso primer valor no coincide con f(i)" ~:(esCaminoFibo [4,7,11] 3) ~?= False,
  "Caso tramo largo empezando en i = 2" ~:(esCaminoFibo [1,2,3,5,8] 2) ~?= True
  ]

-- ejercicio 9
test9:: Test
test9 = test [
  "Propios de 1" ~:(divisoresPropios 1) ~?= [],
  "Propios de 10" ~:(divisoresPropios 10) ~?= [1,2,5],
  "Propios de 25" ~:(divisoresPropios 25) ~?= [1,5]
  ]

-- ejercicio 10
test10:: Test
test10 = test [
  "Enunciado" ~:(sonAmigos 220 284) ~?= True,
  "Enunciado al reves" ~:(sonAmigos 284 220) ~?= True,
  "Segundo par conocido de numeros amigos (1184 y 1210)" ~: (sonAmigos 1184 1210) ~?= True,
  "Numeros cualesquiera que NO son amigos" ~: (sonAmigos 10 20) ~?= False,
  "Numeros muy cercanos que NO son amigos" ~: (sonAmigos 220 285) ~?= False,
  "Un numero perfecto con otro (6 y 28 no son amigos entre si)" ~: (sonAmigos 6 28) ~?= False,
  "Valores minimos distintos permitidos por el requiere (1 y 2)" ~: (sonAmigos 1 2) ~?= False
  ]

test11:: Test
test11 = test [
  "0 perfectos" ~:(losPrimerosNPerfectos 0) ~?= [],
  "1 perfecto" ~:(losPrimerosNPerfectos 1) ~?= [6],
  "2 perfectos" ~:(losPrimerosNPerfectos 2) ~?= [6,28],
  "3 perfectos" ~:(losPrimerosNPerfectos 3) ~?= [6,28,496]
  ]
  
test12:: Test
test12 = test [
  "Inicial" ~:(listaDeAmigos [220, 284, 6, 12, 1184, 1210]) ~?= [(220,284),(1184,1210)],
  "Sin amigos" ~:(listaDeAmigos [1,2,3,4,5]) ~?= [],
  "Solo 2" ~:(listaDeAmigos [220, 284, 6, 12]) ~?= [(220,284)],
  "Raro" ~:(listaDeAmigos [6, 12,284, 5,220]) ~?= [(284,220)]
  ]

allTests :: Test
allTests = test [test1,test2,test3,test4,test5,test6,test7,test8,test9,test10,test11,test12]