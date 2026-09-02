![imagen](https://elc.github.io/blog/images/haskell_python/haskell_python_headerimage.png)
# Practicas Introducción a la programación

Practicas resueltas para la materia de Introducción a la programación. Las practicas corresponden al segundo cuatrimeste de 2026. El codigo de las distintas practicas se realiza con Haskell y Python.

## Contenidos
* practicaIII.hs: Introducción a Haskell
* practicaIV.hs: Recursión sobre números enteros

## Funciones permitidas en Haskell

```haskell
mod :: Integral a => a -> a -> a
div :: Integral a => a -> a -> a
fst :: (a, b) -> a
snd :: (a, b) -> b
sqrt :: Floating a => a -> a
(:) :: a -> [a] -> [a]
(++) :: [a] -> [a] -> [a]
head :: [a] -> a
tail :: [a] -> [a]
fromIntegral :: (Integral a, Num b) => a -> b
fromInteger :: Num a => Integer -> a
not :: Bool -> Bool
```
Ademas, ariméticas (+,-,*,/) y lógicas (&&,||,==,/=,>,<,>=,<=).







