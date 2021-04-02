from model import inpt, resta_fechas, numeros_a_romanos

def main():
    lista_fechas = inpt()
    
    numero_convert = resta_fechas(lista_fechas)

    cant_simbolos = numeros_a_romanos(numero_convert)

    print("La cantidad de simbolos que necesitas es: ", cant_simbolos)

if __name__ == "__main__":
    main()