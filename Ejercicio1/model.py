lista_orden_matirces = [] # Resguardo de cada orden en Strings

estados_fin = { # Diccionario con estados finales
    "0":"R",
    "1":"D",
    "2":"L",
    "3":"U"
}

def inpt(): # Datos de entrada
    try:
        numero_casos = int(input("numero de casos \n>:"))
        if numero_casos <= 0:
            print("Tu dato esta corrupto")
            return None
        
        print("\nIntroduce ahora los valores de cada caso, separados por un espacio\n")
        for i in range(numero_casos):
            orden = input()

            digitos = orden.split(" ", 1)
            if len(digitos) != 2: 
                # comprobacion del espacio entre los numeros
                print("Tu dato esta corrupto")
                return None 
            
            lista_orden_matirces.append(orden) 


        return lista_orden_matirces

    except:
        print("Error en la recoleccion de datos asegurate de introducirlos como se te pide")
        print("Ejemplo: 2 \n 1 2 \n 2 4")

def tipo_mat(orden): 
    # Comprobacion de tipo de matriz (cuadrada o nxm) 
    # retorno de listas con [tipo, valor, valor] 
    try:
        dig_orden = orden.split(" ", 1)
        if int(dig_orden[0]) == int(dig_orden[1]):
            return [0, int(dig_orden[0])]
        else:
            return [1,int(dig_orden[0]),int(dig_orden[1])]
    except:
        print("Error, olvidaste ingresar dos datos correctamente")

def matriz_n(n): # Busqueda del estado final

    if n == 1:
        return estados_fin["0"]
    else:
        estado_fin = 2*n-2 # Formula de la inv
        estado_fin = estado_fin % 4
        estado_fin = estados_fin[str(estado_fin)]
        return estado_fin

def matriz_nxm(n, m): # Busqueda del estado final
    if n < m: 
        estado_fin = 2*n-2
        estado_fin = estado_fin % 4
        estado_fin = estados_fin[str(estado_fin)]
        return estado_fin
    else:
        estado_fin = 2*m-1
        estado_fin = estado_fin % 4
        estado_fin = estados_fin[str(estado_fin)]
        return estado_fin