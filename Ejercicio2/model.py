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
                    break

            fechas.append(int(año))
        return fechas
    except:
        print("Error, escribiste mal los datos de entrada")
