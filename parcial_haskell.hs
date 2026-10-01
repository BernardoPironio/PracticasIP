{-
=========================
    EJERCICIO 1
=========================
problema ejercicio1 (s: seq⟨Z⟩, n: Z) : seq⟨Z⟩ {
  requiere: {existe un índice i tal que 0 ≤ i < |s|-1 y max(s[i], s[i+1]) = n}
  asegura: {|res| = |s| - 2}
  asegura: {res es igual a s sin s[j] ni s[j+1], donde j es una posición válida de s tal que max(s[j], s[j+1]) = n}
}
-}



ejercicio1 :: [Integer] -> Integer -> [Integer]
ejercicio1 [] _ = []
ejercicio1 (x:y:res) n  | maximo [x,y] == n = res
                        | otherwise = x : ejercicio1 (y:res) n

maximo:: [Integer] -> Integer
maximo [x] = x 
maximo (x:xs)   | x > maximo xs = x
                | otherwise = maximo xs

{-
=========================
    EJERCICIO 2
=========================
Conteste marcando la opción correcta.
¿Qué nombre le pondrías a la función del ejercicio anterior?

    SacarTodosLosParesConsecutivosCuyoMaximoEsN
 X  SacarAlgunParConsecutivoCuyoMaximoEsN
    SacarPrimerParConsecutivoCuyoMaximoEsN
    Ninguna de las opciones anteriores describe adecuadamente el problema
-}

{-
=========================
    EJERCICIO 3
=========================
Conteste marcando la opción correcta, teniendo el cuenta el problema ejercicio1
Si s = [7, -2, 7, 1, -5] y n = 7 , entonces:

 X  res1 = [7, 1, -5] es una salida válida
    res2 = [-5] es una salida válida
    No es posible ejecutar la función ya que 7 aparece más de una vez en la secuencia
    Es posible evaluar la función si 7 aparece más de una vez, pero ni res1 ni res2 son soluciones válidas de acuerdo a la especificación    
-}


{-
=========================
    EJERCICIO 4
=========================
Decimos que un número entero positivo es equilibrado si tiene la misma cantidad de dígitos pares (0,2,4,6,8) que de dígitos impares (1,3,5,7,9). Por ejemplo, 1234 tiene dos dígitos pares (2 y 4) y dos impares (1 y 3), por lo tanto es equilibrado.

problema cantidadDeEquilibrados (d: Z, h: Z) : Z {
  requiere: {0 < d ≤ h}
  asegura: {res es la cantidad de números en el rango [d..h] que son equilibrados}
}
-}

cantidadDeEquilibrados :: Integer -> Integer -> Integer
cantidadDeEquilibrados d h  | d > h = 0
                            | cantPares d == cantImpares d = 1 + cantidadDeEquilibrados (d + 1) h
                            | otherwise = cantidadDeEquilibrados (d + 1) h

esPar:: Integer -> Bool
esPar n = mod n 2 == 0

cantPares:: Integer -> Integer
cantPares 0 = 0
cantPares n | esPar (mod n 10) = 1 + cantPares (div n 10)
            | otherwise = cantPares (div n 10)

cantImpares:: Integer -> Integer
cantImpares 0 = 0
cantImpares n  | esPar (mod n 10) == False = 1 + cantImpares (div n 10)
                | otherwise = cantImpares (div n 10)


{-
=========================
    EJERCICIO 5
=========================
Representaremos una nota con una tupla String x Z x Bool, donde:

La primera componente de la tupla contiene el nombre del estudiante
La segunda componente de la tupla contiene la nota del examen
La tercera componente de la tupla indica si el examen es un parcial (True) o un recuperatorio (False)
Se pide implementar aprobaronElParcial, que dada una lista de notas y un umbral de aprobación, devuelva los nombres de los estudiantes que aprobaron al menos un parcial.

problema aprobaronElParcial (notas: seq⟨String x Z x Bool⟩, umbral: Z) : seq⟨String⟩ {
  requiere: {umbral ≥ 0}
  requiere: {notas[i]1 ≥ 0 para todo i tal que 0 ≤ i < |notas|}
  asegura: {res no tiene elementos repetidos}
  asegura: {res contiene los nombres de todos los estudiantes incluidos en notas tales que rindieron al menos un parcial (no recuperatorio) con nota mayor o igual a umbral}
  asegura: {res contiene solamente los nombres de estudiantes que cumplen la condición anterior}
}
-}
aprobaronElParcial :: [(String, Integer, Bool)] -> Integer -> [String]
aprobaronElParcial notas umbral = eliminarRepetidosString (aprobaronElParcialConRepetidos notas umbral)

ejemploNotas = [("mario",10, True),("sofi",2,True),("jhon",10,False),("lu",9,True),("bernie",7,True),("maestroSplinter", 6, True),("mario",7,True)]

nombre:: (String, Integer, Bool) -> String
nombre (x,_,_) = x

valor:: (String, Integer, Bool) -> Integer
valor (_,x,_) = x

enParcial:: (String, Integer, Bool) -> Bool
enParcial (_,_,x) = x

aprobaronElParcialConRepetidos:: [(String, Integer, Bool)] -> Integer -> [String]
aprobaronElParcialConRepetidos [] _ = []
aprobaronElParcialConRepetidos (nota:resto) umbral | valor nota >= umbral && enParcial nota = nombre nota : aprobaronElParcialConRepetidos resto umbral
                                                    | otherwise = aprobaronElParcialConRepetidos resto umbral

pertenece::(Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs)  | e == x = True
                    | otherwise = pertenece e xs

eliminarRepetidosString:: [String] -> [String]
eliminarRepetidosString [] = []
eliminarRepetidosString (x:xs)  | pertenece x xs = eliminarRepetidosString xs
                                | otherwise = x : eliminarRepetidosString xs

{-
=========================
    EJERCICIO 6
=========================
En Haskell, una matriz se puede representar utilizando una secuencia de secuencias, donde cada secuencia interna representa una fila de la matriz. Todas las filas deben tener igual longitud.

problema ejercicio6 (matriz: seq⟨seq⟨Z⟩⟩, n: Z) : seq⟨seq⟨Z⟩⟩ {
  requiere: {|matriz| > 0}
  requiere: {para toda fila perteneciente a matriz, |fila| = |matriz|}
  asegura: {|res| = |matriz|}
  asegura: {para todo i tal que 0 ≤ i < |matriz|, |res[i]| = |matriz[i]|}
  asegura: {para todo i, j tales que 0 ≤ i < |matriz| y 0 ≤ j < |matriz|: si i = j entonces res[i][j] = matriz[i][j] + n, si no res[i][j] = matriz[i][j]}
}
-}

ejercicio6 :: [[Integer]] -> Integer -> [[Integer]]
ejercicio6 matriz n  = sumarADiagonal 0 matriz n

ejemplo = [[1,2,3],[9,8,7],[162,9,17]]


iesimaFila:: Integer -> [[Integer]] -> [Integer]
iesimaFila _ [] = []
iesimaFila i (x:xs) | i == 0 = x
                    | otherwise = iesimaFila (i - 1) xs


sumarNAlElmentoJ:: Integer -> [Integer] -> Integer -> [Integer]
sumarNAlElmentoJ _ [] _ = []
sumarNAlElmentoJ i (x:xs) n | i == 0 = (x + n) : sumarNAlElmentoJ (i - 1) xs n
                            | otherwise = x : sumarNAlElmentoJ (i - 1) xs n

sumarADiagonal:: Integer -> [[Integer]] -> Integer -> [[Integer]]
sumarADiagonal _ [] _ = []
sumarADiagonal k (fila:resto) n = [sumarNAlElmentoJ k fila n] ++ sumarADiagonal (k + 1) resto n
                 
{-
=========================
    EJERCICIO 7
=========================
Conteste marcando la opción correcta.
¿Qué nombre le pondrías a la función del ejercicio anterior?

 X  SumarNALaDiagonal
    SumarNATodaLaMatriz
    ObtenerDiagonal
    Ninguna de las opciones anteriores es un buen nombre para la función
-}

{-
=========================
    EJERCICIO 8
=========================
Tenemos una especificación cuyo único asegura indica res > 100. Creamos un caso de test cuyo resultado esperado es 200, y al ejecutarlo el caso de test falla.
¿Cuál de las siguientes afirmaciones son ciertas?

    El caso de test no está bien diseñado.
    Podría haber un bug en el programa.
 X  Ambas son ciertas (el programa podría tener un bug y además el caso de test no está bien diseñado).
-}