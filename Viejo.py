agst = []  # Lista para el mes de Agosto
sep = []   # Lista para el mes de Septiembre
oct = []   # Lista para el mes de Octubre
nov = []   # Lista para el mes de Noviembre
dec = []   # Lista para el mes de Diciembre

empleadores = ("Levity", "Mulholland", "B&H Construction", "Amazon", "Taco Casa", "Amarak", "Halliburton", "Express", "OU")

fasedicc = {
    "empleador": empleadores,
    "income_2024": [agst, sep, oct, nov, dec]
}

print(fasedicc.keys())

def obtener_ingresos(mes):
    ingresos = []
    empleadores_semanales = []

    for semana in range(1, 5):  # Para cada semana del mes
        # Elegir el empleador
        print(f"\nSemana {semana}:")
        print("Elige el empleador para esta semana:")
        for i, empleador in enumerate(empleadores, start=1):
            print(f"{i}. {empleador}")
        while True:
            try:
                eleccion = int(input("Selecciona el número del empleador: "))
                if 1 <= eleccion <= len(empleadores):
                    empleador_seleccionado = empleadores[eleccion - 1]
                    empleadores_semanales.append(empleador_seleccionado)
                    break
                else:
                    print("Selección inválida. Por favor, elige un número válido.")
            except ValueError:
                print("Por favor, ingrese un número válido.")

        # Ingresar ingresos para la semana actual
        while True:
            try:
                wk_ing = float(input("Introduce tus ingresos: $"))
                ingresos.append(wk_ing)
                mes.append((wk_ing, empleador_seleccionado))
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")
    
    return ingresos, empleadores_semanales

def calcular_gastos_mensuales():
    # Crear un diccionario con los diferentes tipos de egresos
    egresos = {
        'Pagos de Alquiler': 0,
        'Pago del Carro': 0,
        'Comida': 0,
        'Gasolina': 0,
        'Servicios': 0,
        'Pagos de deuda': 0,
        'Renta de Telefono': 0,
        'Pago a mi Novia': 0
    }

    # Solicitar el valor de cada egreso al usuario
    print("Ingrese los gastos mensuales:")
    for egreso in egresos:
        while True:
            try:
                valor = float(input(f"{egreso}: $"))
                egresos[egreso] = valor
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")

    # Calcular la sumatoria de los egresos
    total_gastos = sum(egresos.values())

    # Mostrar el total de los gastos
    print("\nResumen de gastos mensuales:")
    for egreso, valor in egresos.items():
        print(f"{egreso}: ${valor:.2f}")

    print(f"\nTotal de gastos mensuales: ${total_gastos:.2f}")

    return total_gastos, egresos

def calcular_balance(ingresos, egresos):
    ingresos_mensuales = sum(ingresos)  # Sumar ingresos semanales para obtener el total mensual
    balance_mensual = ingresos_mensuales - egresos
    return ingresos_mensuales, balance_mensual

def dar_recomendaciones(balance, ingresos_mensuales):
    porcentaje_ahorro = 0.40 * ingresos_mensuales
    
    if balance > porcentaje_ahorro:
        print("¡Estás ahorrando! Considera ahorrar una cuarta parte para ahorros de emergencia, otra cuarta parte en un ahorro para comprar carro o casa y la otra mitad para uso gozo y disfrute.")
    elif 0 < balance <= porcentaje_ahorro:
        print("¡Buen trabajo! Estás ahorrando, pero podrías ahorrar más.")
    elif balance == 0:
        print("Estás equilibrado. Intenta reducir algunos gastos para ahorrar.")
    else:
        print("Estás gastando más de lo que ingresas. Considera reducir gastos o aumentar tus ingresos.")

def mostrar_resumen_egresos(egresos, ingresos_mensuales):
    # Ordenar los egresos de mayor a menor
    egresos_ordenados = sorted(egresos.items(), key=lambda x: x[1], reverse=True)
    
    # Mostrar el resumen de egresos
    print("\nResumen de egresos:")
    for egreso, valor in egresos_ordenados:
        porcentaje = (valor / ingresos_mensuales) * 100 if ingresos_mensuales > 0 else 0
        print(f"{egreso}: ${valor:.2f} ({porcentaje:.2f}%)")

def main():
    # Elegir el mes correspondiente (aquí solo para Agosto como ejemplo)
    print("Ingresando datos para el mes de Agosto...")
    ingresos, empleadores_semanales = obtener_ingresos(agst)
    total_egresos, egresos = calcular_gastos_mensuales()
    ingresos_mensuales, balance = calcular_balance(ingresos, total_egresos)
    
    print(f"\nIngresos mensuales: ${ingresos_mensuales:.2f}")
    print(f"Tu balance mensual es: ${balance:.2f}")
    dar_recomendaciones(balance, ingresos_mensuales)
    
    print("\nResumen de ingresos y empleadores:")
    for i, (ingreso, empleador) in enumerate(agst, start=1):
        print(f"Semana {i}: Ingreso: ${ingreso:.2f}, Empleador: {empleador}")

    # Mostrar resumen de egresos ordenados y su porcentaje sobre los ingresos
    mostrar_resumen_egresos(egresos, ingresos_mensuales)

if __name__ == "__main__":
    main()