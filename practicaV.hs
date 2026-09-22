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
todosDistintos (x:xs) | pertenece x xs = False
                      | otherwise      = todosDistintos xs

-- (4)
hayRepetidos:: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) | pertenece x xs = True
                    | otherwise      = hayRepetidos xs 

-- (5)
quitar :: (Eq t) => t -> [t] -> [t]
quitar e [] = []
quitar e (x:xs) | e == x    = xs
                | otherwise = x : (quitar e xs)

-- (6)
quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos e (x:xs)  | pertenece e (x:xs) == False = (x:xs)
                      | otherwise                   = quitarTodos e (quitar e (x:xs))

-- (7)
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs)  | hayRepetidos (x:xs) == False = (x:xs)
                          | pertenece x xs == True       = x : eliminarRepetidos (quitar x xs)
                          | otherwise                    = x : eliminarRepetidos xs

-- (8)
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] _          = False
mismosElementos _ []          = False
mismosElementos (x:xs) (y:ys) = todosPertenecen (x:xs) (y:ys) && todosPertenecen (y:ys) (x:xs)


todosPertenecen:: (Eq t) => [t] -> [t] -> Bool
todosPertenecen [] _ = True
todosPertenecen (x:xs) (y:ys) | pertenece x (y:ys) && todosPertenecen xs (y:ys) = True
                              | otherwise                                       = False

-- (9)
capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua (x:xs)  | x == primero (reverso (x:xs)) && capicua (quitar (ultimo xs) xs) = True
                | otherwise = False

primero:: [t] -> t
primero (x:xs) = x

{-
  =========================================
  EJERCICIO 3
  =========================================
-}

-- (1)
sumatoria :: [Integer] -> Integer
sumatoria []     = 0
sumatoria (x:xs) = x + sumatoria (xs)

-- (2)
productoria:: [Integer] -> Integer
productoria []     = 1
productoria (x:xs) = x * productoria xs

-- (3)
maximo :: [Integer] -> Integer
maximo [x]    = x
maximo (x:xs)   | x > maximo xs = x
                | otherwise     = maximo xs 

-- (4)
sumarN:: Integer -> [Integer] -> [Integer]
sumarN _ []     = []
sumarN n (x:xs) = (x + n) : sumarN n xs

-- (5)
sumarElPrimero:: [Integer] -> [Integer]
sumarElPrimero (x:xs) = sumarN x (x:xs)

-- (6)
sumarElUltimo:: [Integer] -> [Integer]
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)

-- (7)
pares:: [Integer] -> [Integer]
pares [] = []
pares (x:xs)  | mod x 2 == 0 = x : pares xs
              | otherwise    = pares xs

-- (8)
multiplosDeN:: Integer -> [Integer] -> [Integer]
multiplosDeN _ [] = []
multiplosDeN n (x:xs) | mod x n == 0 = x : multiplosDeN n xs
                      | otherwise    = multiplosDeN n xs

-- (9)
ordenar :: [Integer] -> [Integer]
ordenar []    = []
ordenar lista = minimo lista : ordenar (quitar (minimo lista) lista)

minimo:: [Integer] -> Integer
minimo [x] = x
minimo (x:xs) | x < minimo xs = x
              | otherwise     = minimo xs

{-
  =========================================
  EJERCICIO 4
  =========================================
-}

-- (1)
--- (a)
sacarBlancosRepetidos:: [Char] -> [Char]
sacarBlancosRepetidos []  = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:resto) | x == ' ' && y == ' ' = sacarBlancosRepetidos (y:resto)
                                  | otherwise            = x : sacarBlancosRepetidos (y:resto)

--- (b)
contarPalabras:: [Char] -> Integer

contarPalabras [x]  | x == ' '  = 0
                    | otherwise = 1
contarPalabras (x:y:resto)  | x /= ' ' && y == ' ' = 1 + contarPalabras (y:resto)
                            | otherwise            = contarPalabras (y:resto)

--- (c)
palabras:: [Char] -> [[Char]]
palabras [] = []
palabras (x:xs) | x == ' ' = palabras xs
                | otherwise = armarPalabra  (x:xs) : palabras (saltarPalabra (x:xs))

armarPalabra:: [Char] -> [Char]
armarPalabra [] = []
armarPalabra (x:resto)  | x == ' ' = []
                        | otherwise = x : armarPalabra (resto)

saltarPalabra:: [Char] -> [Char]
saltarPalabra [] = []
saltarPalabra (x:xs)  | x == ' ' = xs
                      | otherwise = saltarPalabra xs

--- (d)
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga s = palabraMasLargaLista (palabras s)

palabraMasLargaLista :: [[Char]] -> [Char]
palabraMasLargaLista [p] = p
palabraMasLargaLista (p:ps) | largo p > largo (palabraMasLargaLista ps) = p
                            | otherwise                                 = palabraMasLargaLista ps

largo:: [Char] -> Integer
largo []     = 0
largo (x:xs) = 1 + largo xs

--- (e)
aplanar:: [[Char]] -> [Char]
aplanar []     = []
aplanar (x:xs) = x ++ aplanar xs

--- (f)
aplanarConBlancos:: [[Char]] -> [Char]
aplanarConBlancos []     = []
aplanarConBlancos [x]    = x
aplanarConBlancos (x:xs) = x ++ " " ++ aplanarConBlancos xs

--- (g)
aplanarConNBlancos:: [[Char]] -> Integer -> [Char]
aplanarConNBlancos [] _     = []
aplanarConNBlancos [x] _    = x
aplanarConNBlancos (x:xs) n = x ++ nBlancos n ++ aplanarConNBlancos xs n

nBlancos:: Integer -> [Char]
nBlancos 0 = []
nBlancos n = " " ++ nBlancos (n - 1)

{-
  =========================================
  EJERCICIO 5
  =========================================
-}

-- (1)
sumaAcumulada:: (Num t) => [t] -> [t]
sumaAcumulada []       = []
sumaAcumulada [x]      = [x]
sumaAcumulada (x:y:xs) = [x] ++ sumaAcumulada (x + y:xs)

-- (2)
descomponerEnPrimos:: [Integer] -> [[Integer]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = [factorizarEnPrimos x] ++ descomponerEnPrimos xs

factorizarEnPrimos:: Integer  -> [Integer]
factorizarEnPrimos 1 = []
factorizarEnPrimos n = primerPrimo n 2 : factorizarEnPrimos (div n (primerPrimo n 2))

primerPrimo:: Integer -> Integer -> Integer
primerPrimo p k | mod p k == 0 = k
                | otherwise    = primerPrimo p (k + 1)

{-
  =========================================
  EJERCICIO 6
  =========================================
-}

type Texto        = [Char]
type Nombre       = Texto
type Telefono     = Texto
type Contacto     = (Nombre,Telefono)
type ContactosTel = [Contacto] 

elNombre:: Contacto -> Nombre
elNombre (nombre,telefono) = nombre

elTelefono:: Contacto -> Telefono
elTelefono (nombre,telefono) = telefono

-- (a)
enLosContactos:: Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos nombre (contacto:resto)  | nombre == elNombre contacto = True
                                        | otherwise                   = enLosContactos nombre resto

-- (b)
agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto (nombre,telefono) contactos  | enLosContactos nombre contactos == False = contactos ++ [(nombre,telefono)]
                                             | otherwise                                = agregarContacto (nombre,telefono) (eliminarContacto nombre contactos)


-- (c)
eliminarContacto:: Nombre -> ContactosTel -> ContactosTel
eliminarContacto _ [] = []
eliminarContacto nombre (contacto:resto) | nombre == (elNombre contacto) = resto
                                         | otherwise                     = contacto : eliminarContacto nombre resto

{-
  =========================================
  EJERCICIO 7
  =========================================
-}

type Identificacion = Integer
type Ubicacion = Texto
type Disponibilidad = Bool
type Estado = (Disponibilidad,Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]

-- (1)
existeElLocker:: Identificacion -> MapaDeLockers -> Bool
existeElLocker _ [] = False
existeElLocker identificacion (locker:lockers)  | identificacion == (fst locker) = True
                                                | otherwise                      = existeElLocker identificacion lockers

-- (2)
ubicacionDelLocker:: Identificacion -> MapaDeLockers -> Ubicacion
ubicacionDelLocker _ [] = "No existe"
ubicacionDelLocker identificacion (locker:lockers)  | identificacion == (fst locker) = snd (snd locker)
                                                    | otherwise                      = ubicacionDelLocker identificacion lockers

-- (3)
staDisponibleElLocker:: Identificacion -> MapaDeLockers -> Bool
staDisponibleElLocker identificacion (locker:lockers)  | identificacion == (fst locker) = fst (snd locker)
                                                       | otherwise                      = staDisponibleElLocker identificacion lockers

-- (4)
ocuparLocker:: Identificacion -> MapaDeLockers -> MapaDeLockers
ocuparLocker _ [] = []
ocuparLocker identificacion (locker:lockers)  | identificacion == (fst locker) = (identificacion,(False,snd (snd locker))) : lockers
                                              | otherwise                      = locker : ocuparLocker identificacion lockers

{-
  =========================================
  EJERCICIO 8
  =========================================
-}

type Matriz = [[Integer]]
type Fila = [Integer]

-- (1)
sumaTotal :: Matriz -> Integer
sumaTotal []     = 0
sumaTotal (x:xs) = sumarFila x + sumaTotal xs

sumarFila:: Fila -> Integer
sumarFila []     = 0 
sumarFila (x:xs) = x + sumarFila xs

-- (2)
cantidadDeApariciones:: Integer -> [[Integer]] -> Integer
cantidadDeApariciones _ []            = 0
cantidadDeApariciones e (fila:resto)  = cantidadEnFila fila e + cantidadDeApariciones e resto

cantidadEnFila:: Fila -> Integer -> Integer
cantidadEnFila [] _ = 0
cantidadEnFila (x:xs) e | e == x    = 1 + cantidadEnFila xs e
                        | otherwise = cantidadEnFila xs e

-- (3)
contarPalabrasMatriz:: String -> [[String]] -> Integer
contarPalabrasMatriz p [x]          = contarPalabrasFila p x
contarPalabrasMatriz p (fila:resto) = contarPalabrasFila p fila + contarPalabrasMatriz p resto

contarPalabrasFila:: String -> [String] -> Integer
contarPalabrasFila _ [] = 0
contarPalabrasFila p (palabra:resto)  | p == palabra = 1 + contarPalabrasFila p resto
                                      | otherwise    = contarPalabrasFila p resto

-- (4)
cantidadDeApariciones2:: (Eq t) => t -> [[t]] -> Integer
cantidadDeApariciones2 _ []               = 0
cantidadDeApariciones2 e (primera:resto)  = cantidadEnFila2 primera e + cantidadDeApariciones2 e resto


cantidadEnFila2:: (Eq t) => [t] -> t -> Integer
cantidadEnFila2 [] _ = 0
cantidadEnFila2 (primera:resto) e | e == primera = 1 + cantidadEnFila2 resto e
                                  | otherwise    = cantidadEnFila2 resto e

-- (5)
multiplicarPorEscalar:: Integer -> [[Integer]] -> [[Integer]]
multiplicarPorEscalar _ []                = []
multiplicarPorEscalar lambda (fila:resto) = [multiplicarPorEscalarFila lambda fila] ++ multiplicarPorEscalar lambda resto 

multiplicarPorEscalarFila:: Integer -> [Integer] -> [Integer]
multiplicarPorEscalarFila _ []          = []
multiplicarPorEscalarFila lambda (x:xs) = lambda*x : multiplicarPorEscalarFila lambda xs

-- (6)
concatenarFilas:: [[String]] -> String
concatenarFilas []           = ""
concatenarFilas (fila:resto) = concatenar fila ++ concatenarFilas resto
                        

concatenar:: [String] -> String
concatenar []     = []
concatenar (x:xs) = x ++ concatenar xs

-- (7)
iesimaFila:: Integer -> [[a]] -> [a]
iesimaFila _ [] = []
iesimaFila i (fila:resto) | i == 0    = fila
                          | otherwise = iesimaFila (i - 1) resto

-- (8)
iesimaColumna:: Integer -> [[a]] -> [a]
iesimaColumna _ []     = []
iesimaColumna i (x:xs) = elementoFila i x : iesimaColumna i xs

elementoFila:: Integer -> [t] -> t 
elementoFila i (x:xs) | i == 0    = x
                      | otherwise = elementoFila (i - 1) xs

-- (9)
matrizIdentidad:: Integer -> [[Integer]] 
matrizIdentidad n = filaDeFilasIdentidad n n

filaIdentidad:: Integer -> Integer -> Fila
filaIdentidad i k | k == 0    = []
                  | i == k    = 1 : filaIdentidad i (k - 1)
                  | otherwise = 0 : filaIdentidad i (k - 1)

filaDeFilasIdentidad:: Integer -> Integer -> [Fila]
filaDeFilasIdentidad 0 _ = []
filaDeFilasIdentidad i n = [filaIdentidad i n] ++ filaDeFilasIdentidad (i - 1) n  

-- (10)
cantidadParesColumna :: Integer -> [[Integer]] -> Integer
cantidadParesColumna i matriz = cantParesFila (iesimaColumna i matriz)

cantParesFila:: Fila -> Integer
cantParesFila [] = 0
cantParesFila (x:xs)  | mod x 2 == 0 = 1 + cantParesFila xs
                      | otherwise    = cantParesFila xs

{-
  =========================================
  EJERCICIO TIPO PARCIAL
  =========================================
-}

-- Ejercicio de matrices
type MatrizInteger = [[Integer]]

multiplicarFilas:: MatrizInteger -> [Integer]
multiplicarFilas [] = []
multiplicarFilas (x:xs) = productoriaFila x : multiplicarFilas xs

productoriaFila:: Fila -> Integer
productoriaFila [] = 1
productoriaFila (x:xs) = x * productoriaFila xs





