{-
  =========================================
  EJERCICIO 1
  =========================================
-}

fib:: Integer -> Integer
fib n   | n == 0    = 0
        | n == 1    = 1
        | otherwise =  fib (n - 1) + fib (n - 2)

{-
  =========================================
  EJERCICIO 2
  =========================================
-}

parteEntera:: Float -> Integer
parteEntera x   | x < 1     = 0
                | otherwise = 1 + parteEntera (x - 1)

{-
  =========================================
  EJERCICIO 3
  =========================================
-}

esDivisible:: Integer -> Integer -> Bool
esDivisible a b | a - b == 0  = True
                | (a - b) < 0 = False
                | otherwise   = esDivisible (a - b) b

{-
  =========================================
  EJERCICIO 4
  =========================================
-}

sumaImpares:: Integer -> Integer
sumaImpares n   | n == 0    = 0
                | otherwise = 2*n - 1 + sumaImpares (n - 1)
    
{-
  =========================================
  EJERCICIO 5
  =========================================
-}

medioFact:: Integer -> Integer
medioFact n | n == 0 || n == 1 = 1
            | otherwise = n*(medioFact (n - 2))

{-
  =========================================
  EJERCICIO 6
  =========================================
-}


todosDigitosIguales:: Integer -> Bool
todosDigitosIguales n | div n 10 == 0 = True
                      | otherwise     = mod n 10 == mod (div n 10) 10 && todosDigitosIguales (div n 10)

{-
  =========================================
  EJERCICIO 7
  =========================================
-}

cantDigitos:: Integer -> Integer
cantDigitos n | div n 10 == 0 = 1
              | otherwise     = 1 + cantDigitos (div n 10)

iesimoDigito:: Integer -> Integer -> Integer
iesimoDigito n i = mod (div n( 10^(cantDigitos n - i))) 10

{-
  =========================================
  EJERCICIO 8
  =========================================
-}

sumaDigitos:: Integer -> Integer
sumaDigitos n | div n 10 == 0  = mod n 10
              | otherwise      = mod n 10 + sumaDigitos (div n 10)

{-
  =========================================
  EJERCICIO 9
  =========================================
-}

esCapicua:: Integer -> Bool
esCapicua n = n < 10 || (iesimoDigito n 1  == iesimoDigito n (cantDigitos n) && esCapicua(sacarExtremos n))
  where
    sacarExtremos n = div (mod n (10^(cantDigitos n - 1))) 10

{-
  =========================================
  EJERCICIO 10
  =========================================
-}

-- (a)
f1:: Integer -> Integer
f1 n  | n == 0    = 1
      | otherwise = 2^n + f1 (n - 1)

-- (b)
f2:: Float -> Integer -> Float
f2 q n  | n == 1    = q
        | otherwise = q^n + f2 q (n - 1)

-- (c)
f3:: Float -> Integer -> Float
f3 q n  | n == 1    = q
        | otherwise = q^(2*n) + f3 q (n-1)

-- (d)
f4:: Float -> Integer -> Float
f4 q n  | n == 1    = q^n
        | otherwise = q^(2*n) + f4 q (n-1) 

{-
  =========================================
  EJERCICIO 11
  =========================================
-}

-- (a)
eAprox :: Integer -> Float
eAprox n | n <= 0    = 1
         | otherwise = 1 / factorial n + eAprox (n - 1)
  where
    factorial :: Integer -> Float
    factorial 0 = 1
    factorial x = fromInteger x * factorial (x - 1) 

-- (b)
e:: Float
e = eAprox 10

{-
  =========================================
  EJERCICIO 12
  =========================================
-}

raizDeDosAprox:: Integer -> Float
raizDeDosAprox n  | n == 1    = 2
                  | otherwise = 2 + 1/(raizDeDosAprox (n-1)) 

{-
  =========================================
  EJERCICIO 13
  =========================================
-}

f:: Integer -> Integer -> Integer
f n m | n == 1    = sumaSobreM 1 m
      | otherwise = sumaSobreM n m + f (n-1) m
  where
    sumaSobreM n m  | m == 1    = n 
                    | otherwise = n^m + sumaSobreM n (m - 1)

{-
  =========================================
  EJERCICIO 14
  =========================================
-}

sumaPotencias:: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m = (sumaN q n)*(sumaN q m)
  where
    sumaN q n | n == 1     = q
              | otherwise  = q^n + sumaN q (n-1) 

{-
  =========================================
  EJERCICIO 15
  =========================================
-}

sumaRacionales :: Integer -> Integer ->Float
sumaRacionales n m  | n == 1    = sumaM n m
                    | otherwise = sumaM n m + sumaRacionales (n-1) m
  where
    sumaM:: Integer -> Integer -> Float
    sumaM n m | m == 1    = fromIntegral n 
              | otherwise = fromIntegral n/fromIntegral m + sumaM n (m-1)

{-
  =========================================
  EJERCICIO 16
  =========================================
-}

-- (a)
menorDivisor:: Integer -> Integer 
menorDivisor n  | n == 1    = 1
                | otherwise = menorDivisorDesde n 2 
  where
    menorDivisorDesde n k | mod n k == 0 = k 
                          | otherwise    = menorDivisorDesde n (k + 1)

-- (b)
esPrimo:: Integer -> Bool
esPrimo n | n == 1              = False
          | menorDivisor n == n = True
          | otherwise           = False

-- (c)
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos a b | a == 1 || b == 1 = True
                | otherwise        = revisar 2
    where
        revisar k
            | k == a || k == b                 = True
            | a `mod` k == 0 && b `mod` k == 0 = False
            | otherwise                        = revisar (k + 1)

-- (d)
nEsimoPrimo:: Integer -> Integer
nEsimoPrimo n  | n == 1 = 2
            | otherwise = siguientePrimoDesde (nEsimoPrimo (n-1) + 1)
  where 
    siguientePrimoDesde n | esPrimo n = n
                          | otherwise = siguientePrimoDesde (n+1)

{-
  =========================================
  EJERCICIO 17
  =========================================
-}

esFibonacci :: Integer -> Bool
esFibonacci n = esFibonacciAux n 0 1
  where
    esFibonacciAux :: Integer -> Integer -> Integer -> Bool
    esFibonacciAux n a b
      | a == n    = True
      | a > n     = False
      | otherwise = esFibonacciAux n b (a + b)

{-
  =========================================
  EJERCICIO 19
  =========================================
-}

--esSumaInicialDePrimos:: Integer -> Bool
--esSumaInicialDePrimos n | n - sumaPrimos(1) < 0 = False
 --                       | otherwise = n == 
 
--sumaPrimos:: Integer -> Integer 
--sumaPrimos n | n == 0 = 0
--              | otherwise = nEsimoPrimo n + sumaPrimos (n-1) 


