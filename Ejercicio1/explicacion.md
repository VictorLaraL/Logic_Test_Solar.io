# Ejercico 1

### Solucion del ejercicio 1 del repositorio: https://bitbucket.org/ManuelCan/logic/src/master/

Considero que un problema puede resolverse algorítmicamente de muchas maneras, el número de maneras casi siempre se ve determinado por las variables que acompañan al problema, en este caso en específico, después de un análisis cualitativo del problema pensé en 3 formas posibles de hacerlo, de arriba hacia abajo podemos ver como incrementa la complejidad de la solución pero a su vez decrementa el gasto computacional (memoria, procesamiento):

* Por fuerza bruta: escribir código y entrelazar numerosas estructuras de datos sin que estén precisamente organizadas.
* Por estructuras de datos: Diseñar las estructuras de datos correctas y organizarlas para mejorar el rendimiento del algoritmo
* Análisis de patrones: En este caso antes de pensar algorítmicamente, damos un paso atrás y después de estudiar las numerosas situaciones a través de ejemplos prácticos, encontramos patrones o variables sujetas a otras que nos ayudan a determinar un patrón o modelo (posiblemente fórmula o funcion) sin la necesidad de estructuras de datos tan complejas o en su caso algunas implementadas con una carga de cómputo bajo.
	
A continuación muestro como me decidí por  esta última y como fue el proceso de desarrollo, justificación e implementación de estos patrones repetitivos dentro del planteamiento del problema.

Para encontrar un modelo matemático que nos ayude a resolver este planteamiento o problema, subdividi la solución a dos situaciones específicas a manera de dividir la problemática en cuestiones más pequeñas que en conjunto resuelven el problema en su totalidad (metodo Top button). Antes de plantear la solución debemos entender algunos conceptos:
* estado: Nombre para identificar cada vez que se realiza un giro.
* orden: Nombre del concepto asociado a el número de filas y columnas dentro de la matriz.

Ya con estos conceptos bien definidos, procedemos a presentar la solución:


### Orden nxn (matriz cuadrada)
 Después de realizar ejemplos prácticos con n < 10 encontramos un patrón asociado a esta misma variable, es decir:
 	
    -> n está asociada con el número de estados dentro de la matriz

exceptuando el caso de orden 1x1, es decir, n=1 donde se mantiene en el estado inicial.
Tomando el estado incial en cuenta (el estado inicial que es el de la posición 0,0), encontramos una relación de estados dada por 2n-1, es decir:

	-> 2n-1 = número de estados en la matriz, con n >= 2

Pero, a la hora de encontrar el estado final dentro de las matrices de nxn, encontramos que utilizar el estado inicial, corrompe la búsqueda del estado final, por tanto lo eliminamos, arrojándonos una relación de: 

	->2n-2 = número de estados, con n >= 2

Ahora bien, para que esta afirmación sea correcta, corresponde hacer una demostracion por induccion (o algun otro metodo de demostracion), para justificar este patrón, pero por fines prácticos y de tiempo tomaremos esta afirmación como correcta sustentada por ejemplos con n <= 10 ( Pero no lo dejare ahi y aqui encontraran la demostración en unos dias ).

Continuando con la búsqueda del estado final, podemos observar que cada 4 estados se regresa al estado inicial, es por esto que intuí que al hacer la operación módulo (%) 4 al número de estados, nos arrojaría tan solo un entero del 0 al 3, y cada número indica un estado posible:
* 0 = estado inicial R
* 1 = D
* 2 = L
* 3 = U

	-> Por lo tanto, (2n-2) % 4 = estado final, dentro del rango [0,3]

### Orden nxm
En esta situación con matriz de orden que no es específicamente cuadrada ( o mejor dicho, son todos los demás casos fuera del orden cuadrático), existe un patrón especialmente interesante que determina el estado final.

De nueva forma empleamos ejemplos prácticos, haciendo matrices con m fija y n hasta x números, luego por su contraparte n fija y m hasta x números. Dentro de estos ejemplos encontramos una situación característica:
* cuando m era fija y n > m, el número de estados permanecía intacto, es decir, eran los mismos sin importar el valor de n
* cuando n era fija y m > n, sucedía lo mismo, en este caso sin importar el valor de n, el número de estados era el mismo
* Pero, si invertimos el valor de n y m, no nos arrojaba la misma cantidad de estados (Punto interesante a denotar puesto que interviene en la solución general)

Ahora bien, podemos decir que el valor entre n y m que sea menor, determina la cantidad de estados dentro de la matriz (Contando con el estado inicial 0,0).

    -> el menor valor entre m y n, determina la cantidad de estados

pero dependiendo de cual de estos dos valores sea el menor, se tiene una relación diferente, veamos que pasa en cada caso:

* Cuando n es menor, existe una relación entre el número de estados de la forma 2n
* Cuando m es menor, existe una relación entre el número de estados de la forma 2n+1

    -> si n<m: 2n-1 = número de estados
    -> si m<n: 2m = número de estados 

De nueva cuenta estas relaciones (funciones o fórmulas) no podemos tomarlas como certezas hasta probarlas, necesitamos demostrarlas por inducción (o algun otro metodo de demostracion) para justificarlas, pero de nuevo por fines prácticos y de tiempo se tomará como una certeza después de haber probado los posibles casos con  1 <= n,m <= 10 (De igual forma se realizará la demostración en días posteriores).

Una vez determinado el número de estados, dependiendo de las condiciones, podemos utilizar el mismo método para determinar el estado final que vimos en las matrices de orden cuadrado, puesto que cumple con la misma condición que cada 4 estados se regresa al estado inicial.

	-> (2n-1) o (2m) % 4 = estado final, dentro del rango [0,3]
