import Data.Ratio

{-
  =========================================
  EJERCICIO 1
  =========================================
-}

-- (a)
f:: Integer -> Integer
f x | x == 1  = 8
    | x == 4  = 131
    | x == 16 = 16

-- (b)
g:: Integer -> Integer
g x | x == 8   = 16
    | x == 16  = 4
    | x == 131 = 1

-- (c)
h:: Integer -> Integer
h x = (f.g) x

k:: Integer -> Integer
k x = g (f x)

{-
  =========================================
  EJERCICIO 2
  =========================================
-}

-- (a)
absoluto:: Integer -> Integer
absoluto x | x < 0  = -x
           | x >= 0 = x

-- (b)
maximoAbsoluto:: Integer -> Integer -> Integer
maximoAbsoluto x y  | absoluto x < absoluto y  = absoluto y
                    | absoluto x >= absoluto y = absoluto x

-- (c)
maximo3:: Integer -> Integer -> Integer -> Integer 
maximo3 x y z   | x >= y && x >= z = x
                | y >= x && y >= z = y
                | z >= x && z >= y = z

-- (d)
algunoEsCero:: Float -> Float -> Bool 
algunoEsCero x y    | x == 0 || y == 0   = True
                    | otherwise          = False

-- (e)
ambosSonCero:: Float -> Float -> Bool
ambosSonCero x y    | x == 0 && y == 0 = True
                    | otherwise        = False

-- (f)
enMismoIntervalo:: Float -> Float -> Bool
enMismoIntervalo x y    | x <= 3 && y <= 3                  = True
                        | x <= 7 && x > 3 && y <= 7 && y >3 = True
                        | x > 7 && y > 7                    = True
                        | otherwise                         = False

-- (g)
sumaDistintos:: Integer -> Integer -> Integer -> Integer
sumaDistintos x y z | x /= y && x /= z && y /= z  = x + y + z
                    | x == y && x /= z && y /= z  = z
                    | x /= y && x == z && y /= z  = y
                    | x /= y && x /= z && y == z  = x 
                    | x == y && x == z && y == z  = 0

-- (h)
esMultiploDe:: Integer -> Integer -> Bool
esMultiploDe x y = mod x y == 0 

-- (i)
digitoUnidades:: Integer -> Integer
digitoUnidades x = mod x 10

-- (j)
digitoDecenas:: Integer -> Integer
digitoDecenas x = digitoUnidades (div x 10)

{-
  =========================================
  EJERCICIO 3
  =========================================
-}

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b | a == 0 || b == 0   = False 
                      | (-a) `mod` b == 0  = True
                      | otherwise          = False

{-
  =========================================
  EJERCICIO 4
  =========================================
-}

-- (a)
productoInterno:: (Float,Float) -> (Float,Float) -> Float
productoInterno (x,y) (z,k) = x*z + y*k
