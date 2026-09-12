{-
  =========================================
  EJERCICIO 1
  =========================================
-}

-- (1)
longitud:: [t] -> Integer
longitud []     = 0
longitud (x:xs) = 1 + longitud (xs)

-- (2)
ultimo:: [t] -> t
ultimo [x]    = x
ultimo (x:xs) = ultimo xs

-- (3)
principio:: [t] -> [t]
principio [x]    = []
principio (x:xs) = x : principio xs

-- (4)
reverso:: [t] -> [t]
reverso []     = []
reverso [x]    = [x] 
reverso (x:xs) = reverso xs ++ [x]

{-
  =========================================
  EJERCICIO 2
  =========================================
-}

-- (1)
pertenece:: (Eq t) => t -> [t] -> Bool
pertenece _ []                  = False
pertenece e (x:xs)  | e == x    = True
                    | otherwise = pertenece e xs

-- (2)
todosIguales:: (Eq t) => [t] -> Bool
todosIguales []       = True
todosIguales [_]      = True
todosIguales (x:y:xs) = x == y && todosIguales (y:xs)

-- (3)
todosDistintos:: (Eq t) => [t] -> Bool
todosDistintos []       = True
todosDistintos [_]      = True


-- (5)
--quitar :: (Eq t) => t -> [t] -> [t]
--quitar e [] = []
--quitar e (x:xs) | e == xs = xs
--                | otherwise = x:(quitar e xs)



{-
  =========================================
  EJERCICIO 3
  =========================================
-}

-- (1)
sumatoria :: [Integer] -> Integer
sumatoria []     = 0
sumatoria (x:xs) = x + sumatoria (xs)

-- (3)
--maximo :: [Integer] -> Integer
--maximo (x)    = x
--maximo (x:xs)   | x > maximo xs = x
--                | otherwise     = maximo xs 
-- (9)
--ordenar :: [Integer] -> [Integer]
--ordenar

{-
  =========================================
  PROBLEMA PRÁCTICA
  =========================================
-}

-- problema sumarnACadaElemento(n: T, s:seq<T>): seq<T>{
--    requiere = {Ture}
--    asegura = {|res| = |s| y cada elemento de res es el elemento de s en ese lugar sumado de n }}

sumarnACadaElemento:: Integer -> [Integer] -> [Integer]
sumarnACadaElemento n [] = []
sumarnACadaElemento n (x:xs) = (x + n): sumarnACadaElemento n xs 

-- problema pertenece(e: T, s:seq<T>): Bool{
--    requiere = {Ture}
--    asegura = {res = true <-> e in s}}

--pertenece :: Eq t => t -> [t] -> Bool
--pertenece n [] = False
--pertenece n (x:xs)  | n == x = True
--                    | otherwise = pertenece n xs

{-
  =========================================
  EJERCICIO TIPO PARCIAL
  =========================================
-}

-- Ejercicio de matrices

type MatrizInteger = [[Integer]]

--multiplicarFilas:: MatrizInteger -> Integer
--multiplicarFilas [fila] = [productoria fila]
--multiplicarFilas (fila:matriz) = productoria fila : multiplicarFilas matriz

productoria:: [Integer] -> Integer
productoria [n] = n
productoria (n:ns) = n*(productoria ns)

-- Cantidad de apariciones
cantidadDeApariciones:: Integer -> MatrizInteger -> Integer
cantidadDeApariciones e [fila] = cantidadDeAparicionesEnFila e fila
cantidadDeApariciones e (fila:matriz) = cantidadDeAparicionesEnFila e fila + cantidadDeApariciones e matriz

cantidadDeAparicionesEnFila:: Integer -> [Integer] -> Integer
cantidadDeAparicionesEnFila _ [] = 0
cantidadDeAparicionesEnFila e (n:ns)  | n == e = 1 + cantidadDeAparicionesEnFila e ns
                                | otherwise = cantidadDeAparicionesEnFila e ns