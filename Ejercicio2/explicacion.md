# Ejercicio2

En este ejercicio, voy a establecer lo entendido del planteamiento puesto que al no recibir respuesta sobre mi duda comenzaré a emplear lo que considero que es la problemática.

En particular entiendo que el problema trata de calcular la cantidad de años entre un periodo A y B y con esto buscar la conversión a números romanos, todo esto para determinar la cantidad de símbolos que se necesitan para almacenar dicha fecha en un DB.

En este caso es importante conocer bastante bien el esquema de números romanos, la cantidad de símbolos que manejan y su interpretación o traducción a nuestro sistema decimal. Para ejemplificar esto tenemos una tabla que nos ayuda a entender la simbología:

![roman.png](img/roman.png)

fuente: https://en.wikipedia.org/wiki/Roman_numerals

como podemos observar el sistema tiene una base 10, esto quiere decir que cada que nuestra cifra sube 10 veces tenemos un nuevo símbolo, además queda decir que cada símbolo no se puede repetir más de 3 veces ( exceptuando algunos casos específicos ).

Con estos datos y por el margen de tiempo para resolver el problema, procedí a realizar un algoritmo “instantáneo” con estas reglas y que haga un recorrido por los años previamente calculados, es decir, primero recopilamos los datos de entrada, hacemos los cálculos restando la fecha de inicio y fin, después con la cantidad de años ya conocida procedemos a dividir dicho número para calcular el número de símbolos necesario.

## Implementacion
Despues de una previa instalacion de Python en el PC donde se utilice el programa, procedemos a abrir un shell y dentro de la carpeta donde está el modulo main.py, escribimos:

```
    python main.py
```

por ultimo queda utilizar el programa como se indica dentro del mismo.