{-
  =========================================
  EJERCICIO 1
  =========================================
-}

sumDivProp:: Integer -> Integer -> Integer
sumDivProp n k  | k == n = 0
                | mod n k == 0 = k + sumDivProp n (k + 1)
                | otherwise = sumDivProp n (k + 1)

esAbundante:: Integer -> Bool
esAbundante n  = sumDivProp n 1 > n

f1:: Integer -> Integer -> Integer
f1 d h  | d == h && esAbundante d = 1
        | d == h = 0
        | esAbundante d = 1 + f1 (d + 1) h
        | otherwise = f1 (d + 1) h


