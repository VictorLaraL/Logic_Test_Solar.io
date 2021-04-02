from model import inpt, tipo_mat, matriz_n, matriz_nxm

def main(): # Funcion pricipal, vista de consola que recolecta los datos de entrada
    
    lista_ordenes = inpt() # Pedimos datos

    for orden in lista_ordenes:
        # Ciclo donde definimos el orden y el tipo de solucion 
        # haciendo llamados a las funciones dentro del modulo model
        
        tipo = tipo_mat(orden)
        if tipo[0] == 0:
            estado_fin = matriz_n(tipo[1])
        else:
            estado_fin = matriz_nxm(tipo[1], tipo[2])
        
        print("\n", estado_fin)

if __name__ == ("__main__"):
    main()