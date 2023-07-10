import datetime

asientos_disponibles = [1] * 100
asistentes = []
entradas_vendidas = {'Platinum': 0, 'Gold': 0, 'Silver': 0}
precios = {'Platinum': 120000, 'Gold': 80000, 'Silver': 50000}

def comprar_entradas():
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (entre 1 y 3): "))
    while cantidad < 1 or cantidad > 3:
        cantidad = int(input("Cantidad inválida. Ingrese la cantidad de entradas a comprar (entre 1 y 3): "))

    print("Ubicaciones disponibles:")
    mostrar_ubicaciones()

    for i in range(cantidad):
        ubicacion = int(input("Seleccione una ubicación disponible: "))
        while ubicacion < 1 or ubicacion > 100 or asientos_disponibles[ubicacion-1] == 0:
            ubicacion = int(input("Ubicación inválida o no disponible. Seleccione otra ubicación: "))

        tipo_entrada = obtener_tipo_entrada(ubicacion)
        asientos_disponibles[ubicacion-1] = 0 
        run = input("Ingrese el RUN del asistente (sin guiones ni puntos): ")
        while not validar_run(run):
            run = input("RUN inválido. Ingrese nuevamente el RUN del asistente (sin guiones ni puntos): ")

        asistentes.append({'ubicacion': ubicacion, 'tipo_entrada': tipo_entrada, 'run': run})
        entradas_vendidas[tipo_entrada] += 1

    print("Operación realizada correctamente.")

def mostrar_ubicaciones():
    for i in range(0, 100, 10):
        fila = asientos_disponibles[i:i+10]
        for j, estado in enumerate(fila, start=i+1):
            if estado == 0:
                print('X', end=' ')
            else:
                print(j, end=' ')
        print()

def ver_listado_asistentes():
    if len(asistentes) == 0:
        print("No hay asistentes registrados.")
    else:
        asistentes_ordenados = sorted(asistentes, key=lambda x: x['run'])
        print("Listado de asistentes:")
        for asistente in asistentes_ordenados:
            print(asistente['run'])

def mostrar_ganancias_totales():
    total_ganado = sum([entradas_vendidas[tipo] * precios[tipo] for tipo in entradas_vendidas])
    print("Tipo Entrada\tCantidad\tTotal")
    for tipo, cantidad in entradas_vendidas.items():
        print(f"{tipo}\t\t{cantidad}\t\t${cantidad * precios[tipo]}")
    print(f"TOTAL\t\t{sum(entradas_vendidas.values())}\t\t${total_ganado}")

def obtener_tipo_entrada(ubicacion):
    if ubicacion <= 20:
        return 'Platinum'
    elif ubicacion <= 50:
        return 'Gold'
    else:
        return 'Silver'

def validar_run(run):
    return run.isdigit() and len(run) == 9

def salir():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
    print(f"Gracias por utilizar el sistema, {nombre} {apellido}.")
    print(f"Fecha actual: {fecha_actual}")

while True:
    print("\n--- MENÚ ---")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == '1':
        comprar_entradas()
    elif opcion == '2':
        mostrar_ubicaciones()
    elif opcion == '3':
        ver_listado_asistentes()
    elif opcion == '4':
        mostrar_ganancias_totales()
    elif opcion == '5':
        salir()
        break
    else:
        print("Opción inválida. Intente nuevamente.")
        git@github.com:Tuki0/et.git