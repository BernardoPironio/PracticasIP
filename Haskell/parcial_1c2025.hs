import Test.HUnit
{-
  =========================================
  EJERCICIO 1
  =========================================
-}

hayPrimosGemelos:: Integer -> Integer -> Bool
hayPrimosGemelos d h | d + 2 > h = False
                    | esPrimo d && esPrimo (d + 2) = True
                    | otherwise = hayPrimosGemelos (d + 1) h

esPrimoRecursivo:: Integer -> Integer -> Bool
esPrimoRecursivo 0 _ = False
esPrimoRecursivo 1 _ = False
esPrimoRecursivo n 2 = True
esPrimoRecursivo n k | mod n (k - 1) /= 0 && esPrimoRecursivo n (k - 1) = True
            | otherwise = False

esPrimo:: Integer -> Bool
esPrimo n = esPrimoRecursivo n n

absoluto:: Integer -> Integer
absoluto x   | x < 0 = -x
        | otherwise = x

{-
  =========================================
  EJERCICIO 2
  =========================================
-}

type Materia = [Char]
type Dia = [Char]
type Inicio = Integer
type Fin = Integer
type Cursada = (Materia,Dia,Inicio,Fin)

materiasTurnoTardeConRepetidos:: [Cursada] -> [Materia]
materiasTurnoTardeConRepetidos [] = []
materiasTurnoTardeConRepetidos (x:xs)   | enHorario x = nombre x : materiasTurnoTardeConRepetidos xs
                                        | otherwise = materiasTurnoTardeConRepetidos xs

nombre:: Cursada -> Materia
nombre (materia,_,_,_) = materia

enHorario:: Cursada -> Bool
enHorario (_,_,inicio,fin)  | inicio < 17 && fin > 14 = True
                            | otherwise = False

pertenece::(Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs)  | e == x = True
                    | otherwise = pertenece e xs

eliminarRepetidos:: [Materia] -> [Materia]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs)    | pertenece x xs = eliminarRepetidos xs
                            | otherwise = x : eliminarRepetidos xs

materiasTurnoTarde:: [Cursada] -> [Materia]
materiasTurnoTarde cursada = eliminarRepetidos (materiasTurnoTardeConRepetidos cursada) 

{-
  =========================================
  EJERCICIO 3
  =========================================
-}

sumaTresConsecutivos:: [Integer] -> [Integer]
sumaTresConsecutivos [x,y] = []
sumaTresConsecutivos (x:y:z:resto) = x + y + z : sumaTresConsecutivos (y:z:resto)

maximo:: [Integer] -> Integer
maximo [x] = x 
maximo (x:xs)   | x > maximo xs = x
                | otherwise = maximo xs

maximaSumaDeTresConsecutivos:: [Integer] -> Integer
maximaSumaDeTresConsecutivos lista = maximo (sumaTresConsecutivos lista)

{-
  =========================================
  EJERCICIO 4
  =========================================
-}

type Fila = [Integer]
type Columna = [Integer]
type Matriz = [Fila]

-- Matriz de ejemplo de 3x3 (Lista de listas)
ejemplo = [ [14, 87, 23]
                , [45, 12, 68]
                , [91,  3, 34]
                ]

sumaIesimaColumna:: Matriz -> Integer -> Integer
sumaIesimaColumna matriz col = sumaColumna (iesimaColumna col matriz)

sumaColumna:: Columna -> Integer
sumaColumna [] = 0
sumaColumna (x:xs) = x + sumaColumna xs

iesimaColumna:: Integer -> Matriz -> Columna
iesimaColumna _ [] = []
iesimaColumna i (fila:resto) = iesimoElemento i fila : iesimaColumna i resto

iesimoElemento:: Integer -> Fila -> Integer
iesimoElemento i (x:xs) | i == 1 = x
                        | otherwise = iesimoElemento (i - 1) xs

{-
  =========================================
  TESTS
  =========================================
-}

testEjercicio1:: Test
testEjercicio1 = test [
    "unSoloNumero_noPrimo"              ~: (hayPrimosGemelos 4 4)   ~?= False,
    "unSoloNumero_primo"                ~: (hayPrimosGemelos 5 5)   ~?= False,
    "dNoTanChico_primosVecinosNoGemelos" ~: (hayPrimosGemelos 4 6)  ~?= False,  
    "rangoSinNingunPrimo"               ~: (hayPrimosGemelos 8 10)  ~?= False,
    "rangoConVariosPrimosSinGemelos"    ~: (hayPrimosGemelos 19 29) ~?= False,  -- primos 19,23,29 pero ninguna pareja a distancia 2
    "gemelosJustoEnLosExtremos"         ~: (hayPrimosGemelos 3 5)   ~?= True,   -- 3 y 5
    "gemelosAlPrincipioDelRango"        ~: (hayPrimosGemelos 1 5)   ~?= True,   -- incluye a 3 y 5
    "gemelosAlFinalDelRango"            ~: (hayPrimosGemelos 15 19) ~?= True,   -- 17 y 19
    "gemelosEnElMedioDelRango"          ~: (hayPrimosGemelos 100 110) ~?= True, -- 101,103 y 107,109
    "rangoAmplioConMuchosGemelos"       ~: (hayPrimosGemelos 1 50)  ~?= True,   -- 3-5, 5-7, 11-13, 17-19, 29-31, 41-43
    "dIgualAHConPrimoAisladoGrande"     ~: (hayPrimosGemelos 97 97) ~?= False   -- un solo número, no alcanza
    ]

testEjercicio2:: Test
testEjercicio2 = test [
    "listaVacia" ~: (materiasTurnoTarde []) ~?= [],
    "unaMateriaFueraDeTurnoTarde_antesDelRango" ~: (materiasTurnoTarde [("Analisis I","Lunes",8,10)]) ~?= [],
    "unaMateriaFueraDeTurnoTarde_despuesDelRango" ~: (materiasTurnoTarde [("Fisica I","Martes",18,20)]) ~?= [],
    "unaMateriaJustoEnElBordeIzquierdo_noSolapa" ~: (materiasTurnoTarde [("Quimica","Miercoles",12,14)]) ~?= [],
    "unaMateriaJustoEnElBordeDerecho_noSolapa" ~: (materiasTurnoTarde [("Algebra","Jueves",17,19)]) ~?= [],
    "unaMateriaCoincideExactoConElRango" ~: (materiasTurnoTarde [("Algoritmos","Viernes",14,17)]) ~?= ["Algoritmos"],
    "unaMateriaContenidaEnElRango" ~: (materiasTurnoTarde [("Discreta","Lunes",15,16)]) ~?= ["Discreta"],
    "unaMateriaSolapaParcialAlInicio" ~: (materiasTurnoTarde [("Analisis II","Martes",10,15)]) ~?= ["Analisis II"],
    "unaMateriaSolapaParcialAlFinal" ~: (materiasTurnoTarde [("Fisica II","Miercoles",16,20)]) ~?= ["Fisica II"],
    "unaMateriaAbarcaTodoElRangoYMas" ~: (materiasTurnoTarde [("Termodinamica","Jueves",9,21)]) ~?= ["Termodinamica"],
    "variasMateriasNingunaEnTurnoTarde" ~: (materiasTurnoTarde [("Analisis I","Lunes",8,10), ("Fisica I","Martes",18,20)]) ~?= [],
    "variasMateriasTodasEnTurnoTarde" ~: (materiasTurnoTarde [("Algoritmos","Viernes",14,17), ("Discreta","Lunes",15,16)]) ~?= ["Algoritmos","Discreta"],
    "mezclaDeMateriasEnYFueraDeTurnoTarde" ~: (materiasTurnoTarde [("Analisis I","Lunes",8,10), ("Algoritmos","Viernes",14,17), ("Fisica I","Martes",18,20)]) ~?= ["Algoritmos"],
    "mismaMateriaDosVecesEnTurnoTarde_noSeRepite" ~: (materiasTurnoTarde [("Analisis II","Lunes",14,16), ("Analisis II","Miercoles",15,17)]) ~?= ["Analisis II"],
    "mismaMateriaTresVecesPeroSoloAlgunasEnTurnoTarde" ~: (materiasTurnoTarde [("Fisica I","Lunes",8,10), ("Fisica I","Martes",14,17), ("Fisica I","Jueves",18,20)]) ~?= ["Fisica I"],
    "dosMateriasDistintasEnElMismoHorario" ~: (materiasTurnoTarde [("Algoritmos","Lunes",14,16), ("Discreta","Lunes",14,16)]) ~?= ["Algoritmos","Discreta"]
    ]

testEjercicio3:: Test
testEjercicio3 = test [
    "tresElementos_unicoTrioPosible" ~: (maximaSumaDeTresConsecutivos [1,2,3]) ~?= 6,
    "tresElementosNegativos" ~: (maximaSumaDeTresConsecutivos [-1,-2,-3]) ~?= (-6),
    "tresElementosConCeros" ~: (maximaSumaDeTresConsecutivos [0,0,0]) ~?= 0,
    "maximoAlPrincipio" ~: (maximaSumaDeTresConsecutivos [10,20,30,1,1,1]) ~?= 60,
    "maximoAlFinal" ~: (maximaSumaDeTresConsecutivos [1,1,1,10,20,30]) ~?= 60,
    "maximoEnElMedio" ~: (maximaSumaDeTresConsecutivos [1,5,2,8,3]) ~?= 15,
    "todosLosElementosIguales" ~: (maximaSumaDeTresConsecutivos [4,4,4,4,4]) ~?= 12,
    "mezclaDePositivosYNegativos" ~: (maximaSumaDeTresConsecutivos [-5,10,-3,8,-1,2]) ~?= 15,
    "variosTriosConLaMismaSumaMaxima" ~: (maximaSumaDeTresConsecutivos [5,5,5,5,5,5]) ~?= 15,
    "numerosGrandes" ~: (maximaSumaDeTresConsecutivos [1000000,2000000,3000000]) ~?= 6000000,
    "secuenciaLargaConMaximoUnico" ~: (maximaSumaDeTresConsecutivos [3,1,4,1,5,9,2,6]) ~?= 17,
    "todosNegativosMaximoEsElMenosNegativo" ~: (maximaSumaDeTresConsecutivos [-10,-1,-2,-3,-20]) ~?= (-6)
    ]


testEjercicio4:: Test
testEjercicio4 = test [
    "matrizDeUnaFilaUnaColumna" ~: (sumaIesimaColumna [[5]] 1) ~?= 5,
    "matrizDeUnaFilaVariasColumnas_primeraColumna" ~: (sumaIesimaColumna [[1,2,3]] 1) ~?= 1,
    "matrizDeUnaFilaVariasColumnas_ultimaColumna" ~: (sumaIesimaColumna [[1,2,3]] 3) ~?= 3,
    "matrizDeVariasFilasUnaColumna" ~: (sumaIesimaColumna [[4],[7],[2]] 1) ~?= 13,
    "matrizCuadrada_primeraColumna" ~: (sumaIesimaColumna [[1,2,3],[4,5,6],[7,8,9]] 1) ~?= 12,
    "matrizCuadrada_columnaDelMedio" ~: (sumaIesimaColumna [[1,2,3],[4,5,6],[7,8,9]] 2) ~?= 15,
    "matrizCuadrada_ultimaColumna" ~: (sumaIesimaColumna [[1,2,3],[4,5,6],[7,8,9]] 3) ~?= 18,
    "matrizRectangular_masFilasQueColumnas" ~: (sumaIesimaColumna [[1,2],[3,4],[5,6],[7,8]] 2) ~?= 20,
    "matrizRectangular_masColumnasQueFilas" ~: (sumaIesimaColumna [[1,2,3,4,5],[6,7,8,9,10]] 4) ~?= 13,
    "columnaConValoresNegativos" ~: (sumaIesimaColumna [[1,-2,3],[-4,5,-6],[7,-8,9]] 2) ~?= (-5),
    "columnaConTodosCeros" ~: (sumaIesimaColumna [[1,0,3],[4,0,6],[7,0,9]] 2) ~?= 0,
    "matrizConValoresRepetidos" ~: (sumaIesimaColumna [[2,2],[2,2],[2,2]] 1) ~?= 6,
    "matrizGrandeConMezclaDeSignos" ~: (sumaIesimaColumna [[10,-3],[20,-7],[30,15],[-5,1]] 1) ~?= 55
    ]

allTests :: Test
allTests = test [testEjercicio1, testEjercicio2, testEjercicio3, testEjercicio4]