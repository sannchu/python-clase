# Proyecto: Taquilla de cine
# Autores: Alejandro Sanz y Paulo Gomez

# Estas variables se ponen aqui porque se usan en todo el programa.
# Tambien sirven para mostrar el resumen aunque se consulte antes de vender.
num_entradas_vendidas = 0
num_operaciones_realizadas = 0
total_recaudado = 0.0

# PARTE OPCIONAL
# Contabilizar cuantas entradas se venden de cada tipo.
num_entradas_vendidas_general = 0
num_entradas_vendidas_menores = 0
num_entradas_vendidas_senior = 0
num_entradas_vendidas_infantiles = 0

while True:
    opcion = input(f"""
    ========== TAQUILLA DE CINE ==========
    1. Comprar entradas
    2. Consultar resumen de ventas
    3. Salir
    4. Reiniciar estadisticas
    Selecciona una opcion: """)

    if opcion == "1":
        # Pedimos los datos del cliente y controlamos que sean correctos.
        nombre = input("Ingrese el nombre del cliente: ")

        try:
            edad = int(input("Ingrese la edad del cliente: "))
        except ValueError:
            print("Error: debes introducir una edad entera.")
            continue

        if edad < 0:
            print("Error: la edad no puede ser negativa.")
            continue

        
            while True:
                try:
                    num_entradas = int(input("Ingrese el numero de entradas a comprar: "))
                
                except ValueError:
                    print("Error: el numero de entradas debe ser un numero entero.")
                    continue
                if num_entradas <= 0:
                    print("Error: el numero de entradas debe ser mayor que cero.")
                elif num_entradas > 10:
                    print("Error: no se pueden comprar mas de diez entradas.")
                else:
                    break
        

        # PARTE OPCIONAL
        # Preguntar si el cliente tiene carnet de estudiante.
        carnet_estudiante = input("¿El cliente tiene carnet de estudiante? (s/n): ")

        # Segun la edad, elegimos el tipo de entrada y su precio.
        # Por defecto, el cliente tiene una entrada general.
        tipo_entrada = "General"
        precio_entrada = 9.00

        if edad < 5:
            tipo_entrada = "Infantil gratuita"
            precio_entrada = 0.00
        elif edad >= 5 and edad <= 17:
            tipo_entrada = "Menores"
            precio_entrada = 5.00
        elif edad >= 65:
            tipo_entrada = "Senior"
            precio_entrada = 6.00

        # PARTE OPCIONAL
        # Aplicar un descuento del 10 % si se compran cinco entradas o mas.
        if num_entradas >= 5:
            precio_entrada *= 0.9

        total_compra = num_entradas * precio_entrada
        mensaje_ticket = f"""
            ========== TICKET ==========
            Cliente: {nombre}
            Tipo: {tipo_entrada}
            Precio por entrada: {precio_entrada:.2f} €
            Numero de entradas: {num_entradas}
            TOTAL: {total_compra:.2f} €
            ============================
            """

        # PARTE OPCIONAL
        # Dar la posibilidad de cancelar antes de confirmar la compra.
        validar_compra = input("Quieres validar la compra? (s/n): ").strip().lower()

        if validar_compra == "s":
            # PARTE OPCIONAL
            # Sumar las entradas vendidas de cada tipo para el resumen.
            if tipo_entrada == "General":
                num_entradas_vendidas_general += num_entradas
            elif tipo_entrada == "Menores":
                num_entradas_vendidas_menores += num_entradas
            elif tipo_entrada == "Senior":
                num_entradas_vendidas_senior += num_entradas
            elif tipo_entrada == "Infantil gratuita":
                num_entradas_vendidas_infantiles += num_entradas

            # Actualizar el numero de operaciones, entradas y dinero recaudado.
            num_operaciones_realizadas += 1
            num_entradas_vendidas += num_entradas
            total_recaudado += total_compra
            print(mensaje_ticket)
        elif validar_compra == "n":
            print("Compra cancelada.")
        else:
            print("Respuesta no valida. La compra no se ha confirmado.")

    elif opcion == "2":
        # PARTE OPCIONAL
        # Calcular la recaudacion media, comprobando que haya alguna venta.
        if num_operaciones_realizadas == 0:
            recaudacion_media = 0.0
        else:
            recaudacion_media = total_recaudado / num_operaciones_realizadas

        # Mostrar las ventas acumuladas hasta el momento.
        mensaje_resumen = f"""
            ========== RESUMEN DE VENTAS ==========
            Operaciones realizadas: {num_operaciones_realizadas}
            Entradas vendidas: {num_entradas_vendidas}
            Entradas vendidas por tipo:
                General: {num_entradas_vendidas_general}
                Menores: {num_entradas_vendidas_menores}
                Senior: {num_entradas_vendidas_senior}
                Infantiles gratuitas: {num_entradas_vendidas_infantiles}
            Recaudacion media por operacion: {recaudacion_media:.2f} €
            Recaudacion total: {total_recaudado:.2f} €
            =======================================
        """
        print(mensaje_resumen)

    elif opcion == "3":
        print("Programa finalizado. Gracias por utilizar la taquilla.")
        break

    elif opcion == "4":
        # PARTE OPCIONAL
        # Reiniciar todos los contadores y acumuladores de las ventas.
        num_entradas_vendidas = 0
        num_operaciones_realizadas = 0
        total_recaudado = 0.0
        num_entradas_vendidas_general = 0
        num_entradas_vendidas_menores = 0
        num_entradas_vendidas_senior = 0
        num_entradas_vendidas_infantiles = 0
        print("Estadisticas reiniciadas.")

    else:
        print("Opcion no valida. Selecciona una opcion del 1 al 4.")
