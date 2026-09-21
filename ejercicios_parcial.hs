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

ejemplo = [[13,12,6,4],[1,1,32,25],[9,2,14,7],[7,3,5,16],[27,2,8,18]]

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
masRepetido (x:xs)  = masRepetidoFila (aplanar (x:xs))

masRepetidoFila :: Fila -> Integer
masRepetidoFila [x] = x
masRepetidoFila (x:xs)  | cantElementos x (x:xs) > cantElementos (masRepetidoFila xs) (x:xs) = x
                        | otherwise = masRepetidoFila xs

cantElementos:: Integer -> Fila -> Integer
cantElementos _ [] = 0
cantElementos e (x:xs)  | e == x = 1 + cantElementos e xs
                        | otherwise = cantElementos e xs

aplanar:: Tablero -> [Integer]
aplanar [] = []
aplanar (fila:resto) = fila ++ aplanar resto

{-
  =========================================
  EJERCICIO 7
  =========================================
-}










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
  "Producto con stock menor a 10 (NO se aplica oferta)" ~: (aplicarOferta [("banana", 5)] [("banana", 40.0)]) ~?= [("banana", 40.0)],
  "Producto en lista de precios pero NO en stock (stock = 0, NO se aplica oferta)" ~: (aplicarOferta [("manzana", 15)] [("manzana", 100.0), ("durazno", 30.0)]) ~?= [("manzana", 80.0), ("durazno", 30.0)],
  "Mezcla de productos con y sin oferta conservando el orden de la lista de precios" ~: (aplicarOferta [("manzana", 15), ("pera", 10), ("banana", 20)] [("pera", 50.0), ("manzana", 100.0), ("banana", 10.0)]) ~?= [("pera", 50.0), ("manzana", 80.0), ("banana", 8.0)]
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
  "Ningun numero se repite (todos aparecen 1 vez)" ~: (masRepetido [[1, 2], [3, 4]]) ~?= 4,  -- Valido devolver 1, 2, 3 o 4 por desempate
  "Empate de frecuencia entre dos numeros" ~: (masRepetido [[1, 1, 2], [2, 3, 4]]) ~?= 2,  -- Valido devolver 1 o 2 (ambos aparecen 2 veces)
  "Tablero de 1 fila y varias columnas" ~: (masRepetido [[4, 8, 8, 5]]) ~?= 8,
  "Tablero de varias filas y 1 columna" ~: (masRepetido [[3], [3], [10]]) ~?= 3
  ]


allTests :: Test
allTests = test [test1,test2,test3,test4]