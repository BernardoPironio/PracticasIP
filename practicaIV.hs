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



