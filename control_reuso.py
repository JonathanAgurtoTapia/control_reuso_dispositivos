### TRABAJO FINAL
### FUNDAMENTOS DE PROGRAMACIÓN 1
### Programa de control de reúso de dispositivos médicos quirúrgicos

###------------------------------------------------------------------

# Diccionarios para la recolección de información
dispositivoMedico = {}
usosReusos = {}
procesosEsterilizacion = {}


# Ingreso de datos de un dispositivo nuevo
def registrarDispositivo():
    
    # Solicitar información al usuario
    print("\nPor favor ingrese los datos del dispositivo médico")
    fechaIngreso = input("Fecha de ingreso: ")
    codigo = input("Ingrese un código único: ")
    if codigo in dispositivoMedico: # Verificar que el código no se repita con un if
        print("...No se puede registrar un código ya usado\n")
        return
    nombre = input("Nombre: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    
    # Registrar los datos en el diccionario
    dispositivoMedico[codigo] = {
        "Fecha de ingreso": fechaIngreso,
        "Nombre": nombre,
        "Marca": marca,
        "Modelo": modelo,
        "Usos": 0, # Siempre empezará en cero ya que los dispositivos llegan nuevos
        "Estado de uso": "Sin uso", # Por lo tanto siempre empezará en "Sin uso"
        "Esterilización": "N.A.", # No aplica por ser nuevo
    }

    # Enviar mensaje de confirmación de registro
    print("...Dispositivo registrado\n")


# Ingreso de datos del uso y reúso de los dispositivos
def registrarUsoReuso():
    
    # Solicitar información al usuario
    print("\nPor favor ingrese los datos del uso o reúso del dispositivo")    
    codigo = input("Ingrese código del dispositivo: ")  
    
    if codigo in dispositivoMedico: # Verificar que el código está en el diccionario
        # Si es verdadero seguir solicitando datos
        fechaUsoReuso = input("Fecha de uso o reúso: ")
        nombreCirugia = input("Nombre de la cirugía: ")
        historiaClinica = input("Historia clínica del paciente: ")
        paciente = input("Nombre del paciente: ")
        encuentro = input("Encuentro quirúrgico: ")
        medico = input("Nombre del cirujano: ")
        observaciones = input("Observaciones: ")

        # Registrar los datos en el diccionario
        usosReusos.setdefault(codigo, []).append({
            "Fecha de uso o reúso": fechaUsoReuso,
            "Nombre de cirugía": nombreCirugia,
            "Encuentro": encuentro,
            "Historia clínica": historiaClinica,
            "Paciente": paciente,            
            "Médico": medico,
            "Observaciones": observaciones
        })

        # Aumentar el contador de usos
        dispositivoMedico[codigo]["Usos"] += 1

        # Cambiar el estado de uso si llega a los 5 usos a más
        if dispositivoMedico[codigo]["Usos"] >= 5:
            dispositivoMedico[codigo]["Estado de uso"] = "No reusar"
        else:
            dispositivoMedico[codigo]["Estado de uso"] = "Apto para reúso"

        # Enviar mensaje de resgitro de uso/reúso + estado de uso/reúso actualizado
        print(f"...Uso/reúso registrado. Estado de uso: {dispositivoMedico[codigo]['Estado de uso']}\n")

    else:
        # Enviar mensaje de error
        print("...Dispositivo no registrado")


# Función para registrar un proceso de esterilización.
def registrarEsterilizacion():
    
    # Solicitar información al usuario
    print("\nPor favor ingrese los datos de la esterilización del dispositivo")
    codigo = input("Ingrese código del dispositivo: ")

    if codigo in dispositivoMedico: # Verificar que el código está en el diccionario
        # Si es verdadero seguir solicitando datos
        fechaEsterilizacion = input("Fecha de ingreso a esterilización: ")
        tipoLavado = input("Tipo de lavado realizado: ")
        tiempoLavado = input("Tiempo de lavado (minutos): ")
        secadoEquipo = input("¿Se realizó secado posterior? (Sí/No): ")
        tiempoSecado = input("Tiempo de secado (minutos): ")
        realizoTermodesinfeccion = input("¿Se realizó termodesinfección? (Sí/No): ")
        tiempoTermodesinfeccion = input("Tiempo de termodesinfección (minutos): ")
        temperaturaTermodesinfeccion = input("Temperatura de la termodesinfección: ")
        bioluminiscencia = input("Resultado del examen de Bioluminiscencia (ATP): ")
        metodoEsterilizacion = input("Método de esterilización: ")

        # Cambiar el estado de esterilización
        if bioluminiscencia != "N.A." and not bioluminiscencia.isdigit():
            print("...Error: Ingrese un número o 'N.A.' para Bioluminiscencia.")
            return
        
        elif bioluminiscencia == "N.A.":
            dispositivoMedico[codigo]["Esterilización"] = "N.A."

        elif int(bioluminiscencia) < 100:
            dispositivoMedico[codigo]["Esterilización"] = "Aprobada"

        else:
            dispositivoMedico[codigo]["Esterilización"] = "Desaprobada"
        
        # Registrar los datos en el diccionario
        procesosEsterilizacion.setdefault(codigo, []).append({ #-------------------------------------
            "Fecha de esterilización": fechaEsterilizacion,
            "Tipo de lavado": tipoLavado,
            "Tiempo de lavado": tiempoLavado,
            "¿Secado de equipo'": secadoEquipo,
            "Tiempo de secado": tiempoSecado,
            "¿Realizó termodesinfección'": realizoTermodesinfeccion,
            "Tiempo de termodesinfección": tiempoTermodesinfeccion,
            "Temperatura de termodesinfección": temperaturaTermodesinfeccion,
            "Bioluminiscencia": bioluminiscencia,
            "Método de esterilización": metodoEsterilizacion,
        })

        # Enviar mensaje de resgitro de esterilización
        print(f"...Esterilización registrada. Estado: {dispositivoMedico[codigo]['Esterilización']}\n")
    else:
        print("...Dispositivo no registrado")


# Función para informar el estado de los dispositivos
def informeEstado():

    # Solicitar información al usuario
    codigo = input("Ingrese código del dispositivo: ")
    
    if codigo in dispositivoMedico: # Verificar que el código está en el diccionario
        # Si es verdadero entrega la información
        informacion = dispositivoMedico[codigo]        
        print(f"...Estado de uso: {informacion['Estado de uso']}, Esterilización: {informacion['Esterilización']}\n")
    else:
        print("...Dispositivo no registrado\n")


# Función para informar el uso y reuso de un dispositivo
def informeUsoReuso():

    # Solicitar información al usuario
    codigo = input("Ingrese código del dispositivo: ")
    
    if codigo in dispositivoMedico: # Verificar que el código está en el diccionario
        # Si es verdadero entrega la información
        informacion = usosReusos.get(codigo,[])        
        if informacion:
            print(f"...Informe de uso y reúso del dispositivo {codigo}:\n")
            for id, registro in enumerate(informacion, start=1):
                print(f"Reúso #{id}:")
                for campo, valor in registro.items():
                    print(f" {campo}: {valor}")
                print()  # Salto entre registros
        else:
            print("...Este dispositivo no tiene registros de uso o reúso\n")
    else:
        print("...Dispositivo no registrado\n")


# Función para informar el uso y reuso de un dispositivo
def informeEsterilizacion():

    # Solicitar información al usuario
    codigo = input("Ingrese código del dispositivo: ")
    
    if codigo in dispositivoMedico: # Verificar que el código está en el diccionario
        # Si es verdadero entrega la información
        informacion = procesosEsterilizacion.get(codigo,[])        
        if informacion:
            print(f"...Informe de usos y reúsos del dispositivo {codigo}:\n")
            for id, registro in enumerate(informacion, start=1):
                print(f"Esterilización #{id}:")
                for campo, valor in registro.items():
                    print(f" {campo}: {valor}")
                print()  # Salto entre registros
        else:
            print("...Este dispositivo no tiene registros de procesos de esterilización\n")
    else:
        print("...Dispositivo no registrado\n")


# Menú principal del sistema en bucle
while True:
    # Menú de opciones del menú principal
    print("\nMENÚ PRINCIPAL\n1. Registrar Dispositivo\n2. Registrar Uso\n3. Registrar Esterilización\n4. Informes\n5. Salir y borrar\n")
    
    # Solicitar opción al usuario
    opcionElegida = input("Seleccione una opción: ")

    # Árbol de decisión según opción elegida
    if opcionElegida == "1":
        registrarDispositivo()
    elif opcionElegida == "2":
        registrarUsoReuso()
    elif opcionElegida == "3":
        registrarEsterilizacion()
    elif opcionElegida == "4":
        
        # Menú de opciones de informe
        while True:
            print("1. Informe de estado\n2. Informe de uso y reúso\n3. Informe de esterilizaciones\n4. Volver al menú principal\n")
            
            # Árbol de decisión según subopción elegida
            subOpcion4 = input("Seleccione una opción de informe: ")
            if subOpcion4 == "1":              
                informeEstado()
            elif subOpcion4 == "2":
                informeUsoReuso()
            elif subOpcion4 == "3":
                informeEsterilizacion()
            elif subOpcion4 == "4":
                # Salir del submenú y volver al menú principal
                break
            else:
                # Mensaje de error si la opción no existe
                print("...Opción no válida.\n")

    elif opcionElegida == "5":             
        # Romper bucle y cerrar programa
        print("...Ha salido del programa. Los datos se han borrado por completo.\n")
        break

    else:
        # Mensaje de error si la opción no existe
        print("...Opción no válida.\n")