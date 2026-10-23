
#Estos variables globales, se ponen aqui ya que se van a usar en todo el programa, y no solo en una funcion
#Aparte se usan para poder hacer un resumen de ventas, ya que si no se inicializan aqui, no se podrian usar 
# en la funcion de resumen de ventas si vas directamente a la opcion 2
num_entradas_vendidas = 0
num_operaciones_realizadas = 0
total_recaudado = 0.00

#PARTE OPCIONAL
# Contabilizar las entradas vendidas de cada tipo
num_entradas_vendidas_general = 0
num_entradas_vendidas_menores = 0
num_entradas_vendidas_mayores = 0
num_entradas_vendidas_infantiles = 0

while True:
    opcion = input (f"""
    ========== TAQUILLA DE CINE ==========
    1. Vender entradas
    2. Consultar resumen de ventas
    3. Salir
    4. Reiniciar estadisticas
    Selecciona una opción:""")
    
    if opcion == "1":
        # Solicitar los datos y controlar posibles errores
        nombre = input("Ingrese el nombre del cliente: ")
        
        try:
            edad = int(input("Ingrese la edad del cliente: "))
        except ValueError:
            print("Error: La edad debe ser un número entero.")
            continue
        try:
                while True:
                    num_entradas = int(input("Ingrese el número de entradas a comprar: "))
                    if num_entradas >= 10:
                        print("Error: El número de entradas debe ser menor que 10.")
                    else:
                        break
        except ValueError:
            print("Error: El número de entradas debe ser un número entero.")
            continue

        carnet_estudiante = input("¿El cliente tiene carnet de estudiante? (s/n): ")
        
        
        # Determinar el tipo de entrada y el precio segun la edad
        #Por defecto, ponemos la entrada general
        tipo_entrada = "General"
        precio_entrada = 9.00

        #Aqui hacemos las comprobaciones de edad y determinamos el precio final
        if edad < 5:
            tipo_entrada = "Infantil gratuita"
            precio_entrada = 0.00

        elif 5 < edad and edad < 17:
            tipo_entrada = "Menores"
            precio_entrada = 5.00

        elif edad >= 65:
            tipo_entrada = "Mayores"
            precio_entrada = 6.00
        
        #PARTE OPCIONAL 
        #Aplicar un descuento del 10 % si se compran cinco entradas o mas
        if num_entradas >= 5:
            precio_entrada *= 0.9  

        mensaje = f"""
            ========== TICKET ==========
            Cliente: {nombre}
            Tipo: {tipo_entrada}
            Precio por entrada: {precio_entrada:.2f} €
            Número de entradas: {num_entradas}
            TOTAL: {num_entradas * precio_entrada:.2f} €
            ============================
            """

        #PARTE OPCIONAL
        # Permitir cancelar una compra antes de confirmarla.
        validar_compra = input("Quieres validar la compra? (s/n): ")
        if validar_compra == "s":
            #En este paso lo que hacemos sumar las entradas seleccionadas al contador global de entradas
            if tipo_entrada == "General":
                num_entradas_vendidas_general += num_entradas
            elif tipo_entrada == "Menores":
                num_entradas_vendidas_menores += num_entradas
            elif tipo_entrada == "Mayores":
                num_entradas_vendidas_mayores += num_entradas
            elif tipo_entrada == "Infantil gratuita":
                num_entradas_vendidas_infantiles += num_entradas


            #En este paso lo que hacemos sumar las operaciones realizadas al contador global de operaciones 
            num_operaciones_realizadas += 1
            num_entradas_vendidas += num_entradas
            #En este paso lo que hacemos sumar el total recaudado al contador global de recaudacion
            total_recaudado += num_entradas * precio_entrada
            print(mensaje)
        elif validar_compra == "n":
            
                        
            print("Compra cancelada.")
            
        
        

        
    elif opcion == "2":


        # Mostrar el resumen de ventas
        
        mensaje_resumen = f"""
            ========== RESUMEN DE VENTAS ==========
            Operaciones realizadas: {num_operaciones_realizadas}
            Entradas vendidas: {num_entradas_vendidas}
            Entradas vendidas por tipo:
                General: {num_entradas_vendidas_general}
                Menores: {num_entradas_vendidas_menores}
                Mayores: {num_entradas_vendidas_mayores}
                Infantiles gratuitas: {num_entradas_vendidas_infantiles}
            Recaudacion media por operacion: {total_recaudado / num_operaciones_realizadas}
            Recaudación total: {total_recaudado:.2f} €
            =======================================
        """
        print(mensaje_resumen)
    elif opcion == "3":
        print("Saliendo del programa...")
        break

    elif opcion == "4":
            num_entradas_vendidas = 0.00
            num_operaciones_realizadas = 0.00
            total_recaudado = 0.00

            
            num_entradas_vendidas_general = 0.00
            num_entradas_vendidas_menores = 0.00
            num_entradas_vendidas_mayores = 0.00
            num_entradas_vendidas_infantiles = 0.00
            


