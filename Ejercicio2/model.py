num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]

def inpt(): # Funcion para introducir datos y regresarlos organizados en una lista
    try:
        fechas = []

        datos = input("Introduce las fechas en conjunto pero separadas por un guion (-): \n>: ")
        cdato = datos.split('-', 1)
    
        for i in range(2):
            año = ''
            for simbolo in cdato[i]:
                if simbolo.isdigit():
                    año = año+simbolo
                else:
                    if simbolo == "B":
                        fechas.append("B")
                    else:
                        fechas.append("A")
                    break

            fechas.append(int(año))
        return fechas
    except:
        print("Error, escribiste mal los datos de entrada")

def resta_fechas(lista_fechas): # Calculamos el tiempo restando las fechas dependiendo 
    if lista_fechas[0] == "B" and lista_fechas[2] == "B":
        return lista_fechas[1] - lista_fechas[3]
    elif lista_fechas[0] == "B" and lista_fechas[2] == "A":
        return lista_fechas[1] + lista_fechas[3]
    else:
        return lista_fechas[3] - lista_fechas[1]

def numeros_a_romanos(numero): # Calculamos la cantidad de simbolos mediante la base 10
    simbolos = 0

    i = 12 
    while numero: 

        # Hacemos una division entera tras encontrar su primera base
        div = numero // num[i]

        # Ahora nuestro numero es lo que queda de sustraer su base
        numero %= num[i]

        while div:

            # En esta parte vamos adicionando los simbolos que ya encontramos con la division entera
            simbolos += 1
            div -= 1
            
        i -= 1
    
    return simbolos