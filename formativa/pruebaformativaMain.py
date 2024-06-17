listaTitulo=[]
matriz=[[]]
while True:
    print("**Menu de opciones**\n(1) Registrar trabajador\n(2) Lista de todos los trabajadores\n(3) Imprimir planilla de sueldo \n(4) Salir del programa")
    try:
        op=int(input("Selecciona una opcion:"))
    except ValueError:
        print("Intentelo denuevo")
    else:
        if op==1:
            print("a")
        elif op==2:
            print("a")
        elif op==3:
            print("a")
        elif op==4:
            break
        