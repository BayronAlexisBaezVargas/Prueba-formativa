trabajadores = []
titulo="Nombre,Apellido,cargo,Sueldo en bruto,Desc. salud,Desc. AFP,Liquido a pagar"
cargos = ["CEO", "Desarrollador", "Analista de datos"]

def registrar_trabajador():
    nombre = input("Ingrese el nombre del trabajador: ")
    apellido = input("Ingrese el apellido del trabajador: ")
    
    print("Cargos disponibles:", cargos)
    cargo = input("Ingrese el cargo del trabajador: ")
    while cargo not in cargos:
        print("Cargo no válido. Intente nuevamente.")
        cargo = input("Ingrese el cargo del trabajador: ")
    
    sueldo_bruto = float(input("Ingrese el sueldo bruto del trabajador: "))
    desc_salud = sueldo_bruto * 0.07
    desc_afp = sueldo_bruto * 0.1
    sueldo_liquido = sueldo_bruto - desc_salud - desc_afp
    
    trabajador = {
        "nombre": nombre,
        "apellido": apellido,
        "cargo": cargo,
        "sueldo_bruto": sueldo_bruto,
        "desc_salud": desc_salud,
        "desc_afp": desc_afp,
        "sueldo_liquido": sueldo_liquido
    }
    
    trabajadores.append(trabajador)
    print("Trabajador registrado exitosamente.\n")

def listar_trabajadores():
    if not trabajadores:
        print("No hay trabajadores registrados.\n")
    else:
        print("\nLista de Trabajadores:")
        for trabajador in trabajadores:
            print(f"Nombre: {trabajador['nombre']} {trabajador['apellido']}")
            print(f"Cargo: {trabajador['cargo']}")
            print(f"Sueldo Bruto: {trabajador['sueldo_bruto']}")
            print(f"Desc. Salud: {trabajador['desc_salud']}")
            print(f"Desc. AFP: {trabajador['desc_afp']}")
            print(f"Líquido a pagar: {trabajador['sueldo_liquido']}")
            print()

def imprimir_planilla_a_archivo():
    with open("Planilla_de_Trabajadores.txt","w") as archivo:
        archivo.write(titulo)
        for trabajador in trabajadores:
            archivo.write(f"\n{trabajador["nombre"]} {trabajador["apellido"]} {trabajador['cargo']} {trabajador["sueldo_bruto"]} {trabajador["desc_salud"]} {trabajador['desc_afp']} {trabajador['sueldo_liquido']}")
    print("\nArchivo creado correctamente\n")
def mostrar_menu():
    print("Menú de opciones:")
    print("1. Registrar trabajador")
    print("2. Listar todos los trabajadores")
    print("3. Imprimir planilla de sueldos")
    print("4. Salir del programa")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            registrar_trabajador()
        elif opcion == '2':
            listar_trabajadores()
        elif opcion == '3':
           imprimir_planilla_a_archivo()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.\n")