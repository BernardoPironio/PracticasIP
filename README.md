![imagen](https://elc.github.io/blog/images/haskell_python/haskell_python_headerimage.png)
# Practicas Introducción a la programación

Practicas resueltas para la materia de Introducción a la programación. Las practicas corresponden al segundo cuatrimeste de 2026. El codigo de las distintas practicas se realiza con Haskell y Python.

## Contenidos
### Haskell
* practicaIII.hs: Introducción a Haskell.
* practicaIV.hs: Recursión sobre números enteros.
* practicaV.hs: Recursión sobre listas.
* simulacro_parcial.hs: Simulacro del primer parcial, con casos de test incluidos.
* ejercicios_parcial.hs: Ejercicios tipo parcial, con casos de test incluidos.
* parcial_1c2025.hs: Parcial del primer cuatrimestre de 2025 resuelto, con casos de test incluidos.
* parcial_haskell.hs: Parcial que nos tomaron el segundo cuatrimestre de 2026, con mutiple choice incluido.

### Python
* practicaVI.py: Introducción a Lenguaje Imperativo.
* practicaVII.py: Funciones sobre listas (tipos complejos).

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

## Funciones permitidas en Python

```python
conversión de tipos: (int, list, float, str, tuple, bool)
estructuras: (if-else-elif, while, for) // Pueden usar for in range(..) o for in secuencia
Rango: range(i,f,p) // Pueden usar los 3 parámetros, 2 o 1.
ariméticas (+, -, *, /, //, sqrt, round, floor, ceil, %)
lógicas (and, or, not, ==, !=, >, <, >=, <=)
pertenece: in
concatenacion: +
repeticion: *
longitud: len
acceso a elementos: s[elem] // No está permitido s[i:f], s[-i] o similar!
Listas: append(e), insert(p, e), remove(e), index(e), count(e), clear(), pop(), pop(n), copy()
Diccionarios: items(), keys(), values(), pop(clave), clear()
TAD Pilas: from queue import LifoQueue
pila = LifoQueue(); put(e); get(); empty()
TAD Colas: from queue import Queue
cola = Queue(); put(e); get(); empty()
El uso de break/continue NO está recomendado.
Archivos: open, read, readline, readlines, write, writelines, close, os.path.join(), os.path.exists()
```







