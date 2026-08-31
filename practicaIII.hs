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

-- (b)
esParMenor :: (Float, Float) -> (Float, Float) -> Bool
esParMenor (x,y) (z,k) = x < z && y < k

-- (c)
distancia:: (Float, Float) -> (Float, Float) -> Float
distancia (x,y) (z,k) = sqrt((z-x)^2 + (k-y)^2)

-- (d)
distnanciaTerna:: (Float, Float, Float) -> Float
distnanciaTerna (x,y,z) = x + y + z 

-- (e)
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (x, y, z) k = filtrar x + filtrar y + filtrar z
  where
    filtrar n | mod n k == 0 = n
              | otherwise    = 0

-- (f)
posPrimerPar:: (Integer,Integer,Integer) -> Integer
posPrimerPar (x,y,z)  | par x && par y && par z = 4
                      | par x                   = 1
                      | par y                   = 2
                      | par z                   = 3
  where 
    par n | mod n 2 == 0 = True
          | otherwise    = False

-- (g)
crearPar:: a -> b -> (a,b)
crearPar x y = (x,y)                      

-- (h)
invertir:: (a,b) -> (b,a)
invertir (x,y) = (y,x)

{-
  =========================================
  EJERCICIO 5
  =========================================
-}

f1 :: Integer -> Integer
f1 n | n <= 7   = n^2
    | otherwise = 2*n - 1

g1 :: Integer -> Integer
g1 n | mod n 2 == 0 = div n 2
    | otherwise     = 3*n + 1

todosMenores:: (Integer, Integer, Integer) -> Bool
todosMenores (t0, t1, t2) = (f1 t0 > g1 t0) && (f1 t1 > g1 t1) && (f1 t2 > g1 t2)

{-
  =========================================
  EJERCICIO 6
  =========================================
-}

type Anio       = Integer
type EsBisiesto = Bool


bisiesto:: Anio -> EsBisiesto
bisiesto x  | mod x 4 /= 0 || (mod x 100 == 0 && mod x 400 /= 0) = False
            | otherwise                                          = True

{-
  =========================================
  EJERCICIO 7
  =========================================
-}

type Punto3D = (Float, Float, Float)

distanciaManhattan:: Punto3D-> Punto3D-> Float
distanciaManhattan (x1,y1,z1) (x2,y2,z2) = abs (x1 - x2) + abs (y1 - y2) + abs (z1 - z2) 

{-
  =========================================
  EJERCICIO 8
  =========================================
-}

sumaUltimosDosDigitos:: Integer -> Integer
sumaUltimosDosDigitos x = mod (abs x) 10 + mod (div (abs x) 10) 10

comparar:: Integer -> Integer -> Integer
comparar a b  | sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b) = 1
              | sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b) = -1
              | sumaUltimosDosDigitos(a) == sumaUltimosDosDigitos(b) = 0
