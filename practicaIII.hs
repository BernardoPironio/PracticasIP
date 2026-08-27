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
maximoAbsoluto:: Integer -> Integer
maximoAbsoluto x y  | absoluto x < absoluto y  = absoluto y
                    | absoluto x >= absoluto y = absoluto x

-- (c)
maximo3:: Integer -> Integer 
maximo3 x y z   |