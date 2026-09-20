import Test.HUnit
{-
  =========================================
  EJERCICIO 1
  =========================================
-}

sumDivProp:: Integer -> Integer -> Integer
sumDivProp n k  | k == n       = 0
                | mod n k == 0 = k + sumDivProp n (k + 1)
                | otherwise    = sumDivProp n (k + 1)

esAbundante:: Integer -> Bool
esAbundante n  = sumDivProp n 1 > n

f1:: Integer -> Integer -> Integer
f1 d h  | d == h && esAbundante d = 1
        | d == h                  = 0
        | esAbundante d           = 1 + f1 (d + 1) h
        | otherwise               = f1 (d + 1) h

{-
  =========================================
  EJERCICIO 2
  =========================================
-}

f2:: [(String, Integer, Integer)] -> [String]
f2 [] = []
f2 (x:xs)   | vencida x == False                                                                     = f2 xs
            | vencida x == True && pertenece (primerElemento x) (listaPrimerosElementos xs) == False = (primerElemento x) : f2 xs
            | otherwise                                                                              = f2 xs


vencida:: (String, Integer, Integer) -> Bool
vencida (materia, año, cuatri)  | año < 2021                 = True
                                | año == 2021 && cuatri <= 1 = True
                                | otherwise                  = False

primerElemento:: (String,Integer,Integer) -> String
primerElemento (x,_,_) = x

pertenece:: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs)  | e == x    = True
                    | otherwise = pertenece e xs

listaPrimerosElementos:: [(String,Integer,Integer)] -> [String]
listaPrimerosElementos [] = []
listaPrimerosElementos (x:xs) = primerElemento x : listaPrimerosElementos xs

{-
  =========================================
  EJERCICIO 3
  =========================================
-}

f3:: [Integer] -> Integer -> [Integer]
f3 [] _ = []
f3 (x:xs) u | x < 0 = []
            | x <= u = x : f3 xs u
            | x > u = u : f3 xs u

{-
  =========================================
  EJERCICIO 4
  =========================================
-}

type MatrizInteger = [[Integer]]

f4:: MatrizInteger -> Integer -> Integer
f4 [(x:xs)] col      = unoSiElementoPar (col - 1) (x:xs)
f4 (fila:matriz) col = unoSiElementoPar (col - 1) fila + f4 matriz col

unoSiElementoPar:: Integer -> [Integer] -> Integer
unoSiElementoPar _ [] = 0
unoSiElementoPar n (x:xs)   | n == 0 && mod x 2 ==  0 = 1
                            | n == 0                  = 0
                            | otherwise               = unoSiElementoPar (n - 1) xs

 
-- ---------- Ejercicio 1: f1 (números abundantes) ----------
testsF1 :: Test
testsF1 = test [
    "Caso ejemplo enunciado: f1 12 24" ~: (f1 12 24) ~?= 4,
    "Caso un solo abundante: f1 12 12" ~: (f1 12 12) ~?= 1,
    "Caso sin abundantes: f1 1 11"     ~: (f1 1 11)  ~?= 0,
    "Caso numero perfecto no cuenta: f1 6 6" ~: (f1 6 6) ~?= 0
  ]
 
-- ---------- Ejercicio 2: f2 (materias vencidas) ----------
testsF2 :: Test
testsF2 = test [
    "Caso ejemplo enunciado" ~:
      (f2 [("Algoritmos y Estructuras de Datos I", 2020, 2),
           ("Algoritmos y Estructuras de Datos II", 2022, 1)])
      ~?= ["Algoritmos y Estructuras de Datos I"],
 
    "Caso lista vacia" ~: (f2 []) ~?= [],
 
    "Caso segundo cuatrimestre 2021 vencido (no aparece)" ~:
      (f2 [("Fisica I", 2021, 2)]) ~?= [],
 
    "Caso primer cuatrimestre 2021 no vencido (limite)" ~:
      (f2 [("Fisica I", 2021, 1)]) ~?= ["Fisica I"],
 
    "Caso no repite nombres" ~:
      (f2 [("Analisis I", 1994, 1), ("Analisis I", 1996, 2)])
      ~?= ["Analisis I"]
  ]
 
-- ---------- Ejercicio 3: f3 (prefijo no negativo topeado) ----------
testsF3 :: Test
testsF3 = test [
    "Caso ejemplo enunciado" ~:
      (f3 [3,8,5,0,7,-2,4] 5) ~?= [3,5,5,0,5],
 
    "Caso primer elemento negativo" ~:
      (f3 [-1,2,3] 5) ~?= [],
 
    "Caso lista vacia" ~: (f3 [] 5) ~?= [],
 
    "Caso sin necesidad de topear" ~:
      (f3 [1,2,3,4] 10) ~?= [1,2,3,4],
 
    "Caso todos topeados" ~:
      (f3 [5,9,2] 2) ~?= [2,2,2]
  ]
 
-- ---------- Ejercicio 4: f4 (pares en una columna) ----------
testsF4 :: Test
testsF4 = test [
    "Caso ejemplo enunciado" ~:
      (f4 [[-9,8,2,3],[2,7,-5,3],[-1,0,5,6]] 2) ~?= 2,
 
    "Caso primera columna" ~:
      (f4 [[-9,8,2,3],[2,7,-5,3],[-1,0,5,6]] 1) ~?= 1,
 
    "Caso una sola fila" ~:
      (f4 [[4,7,9]] 1) ~?= 1,
 
    "Caso sin pares" ~:
      (f4 [[1,3],[5,7],[9,11]] 1) ~?= 0
  ]
 
-- ---------- Todos juntos ----------
allTests :: Test
allTests = test [testsF1, testsF2, testsF3, testsF4]
 
main :: IO ()
main = do
  _ <- runTestTT allTests
  return ()
