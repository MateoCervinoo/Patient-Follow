#Funcion Menu
def menu():
    print('\n---Menú de opciones---\n')
    print('1. Cargar paciente nuevo')
    opcion = int(input('Ingrese una opción: '))
    return opcion

def main():
    op = 0
    print("SEGUIMIENTO DE PACIENTES")
    while op != 8:
        op = menu()
        if op == 1:
            print("Cargar paciente nuevo\n")
        elif op == 8:
            print('Guardando datos... Cerrando programa...')
        else:
            print('Error! Opcion no valida.')

if __name__ == '__main__':
    main()