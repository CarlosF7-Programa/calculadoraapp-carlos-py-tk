import tkinter as tk
from tkinter import ttk

def calcular():  # sourcery skip: extract-method
    try:
        # Obtiene los ingresos y egresos del usuario
        ingresos = [float(entry_ingreso_semana[i].get()) for i in range(4)]
        egresos = {
            'Pagos de Alquiler': float(entry_egresos['Pagos de Alquiler'].get()),
            'Pago del Carro': float(entry_egresos['Pago del Carro'].get()),
            'Comida': float(entry_egresos['Comida'].get()),
            'Gasolina': float(entry_egresos['Gasolina'].get()),
            'Servicios': float(entry_egresos['Servicios'].get()),
            'Pagos de deuda': float(entry_egresos['Pagos de deuda'].get()),
            'Renta de Telefono': float(entry_egresos['Renta de Telefono'].get()),
            'Pago a mi Novia': float(entry_egresos['Pago a mi Novia'].get()),
            'Pago Seguro de Carro': float(entry_egresos['Pago Seguro de Carro'].get())
        }

        total_egresos = sum(egresos.values())
        ingresos_mensuales = sum(ingresos)
        balance = ingresos_mensuales - total_egresos

        # Limpiar tablas antes de insertar nuevos datos
        for item in tree_ingresos.get_children():
            tree_ingresos.delete(item)
        for item in tree_egresos.get_children():
            tree_egresos.delete(item)

        # Insertar datos en la tabla de Ingresos
        tree_ingresos.insert("", "end", values=("Ingresos Mensual", "", ingresos_mensuales, "100%"))
        for i, ingreso in enumerate(ingresos):
            tree_ingresos.insert("", "end", values=(f"SEMANA {i+1}", f"B&H {i+1}", ingreso, f"{(ingreso / ingresos_mensuales) * 100 if ingresos_mensuales > 0 else 0:.0f}%"))

        # Insertar datos en la tabla de Egresos
        for egreso, valor in egresos.items():
            porcentaje = (valor / ingresos_mensuales) * 100 if ingresos_mensuales > 0 else 0
            tree_egresos.insert("", "end", values=("", egreso, valor, f"{porcentaje:.1f}%"))
        
        # Agregar totales
        tree_egresos.insert("", "end", values=("Saldo Restante", "", balance, f"{(balance / ingresos_mensuales) * 100 if ingresos_mensuales > 0 else 0:.1f}%"))
        tree_egresos.insert("", "end", values=("Gastos Totales", "", total_egresos, f"{(total_egresos / ingresos_mensuales) * 100 if ingresos_mensuales > 0 else 0:.1f}%"))

    except ValueError:
        resultado.set("Por favor, ingrese valores numéricos válidos.")
        recomendacion.set("")
        resumen.set("")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Ingresos y Egresos")

entry_ingreso_semana = []
entry_egresos = {}

# Crear entradas para los ingresos semanales
for i in range(4):
    tk.Label(root, text=f"Ingreso Semana {i+1}:").grid(row=i, column=0, padx=5, pady=5)
    entrada = tk.Entry(root)
    entrada.grid(row=i, column=1, padx=5, pady=5)
    entry_ingreso_semana.append(entrada)

# Crear entradas para los egresos
egreso_labels = ['Pagos de Alquiler', 'Pago del Carro', 'Comida', 'Gasolina', 'Servicios', 'Pagos de deuda', 'Renta de Telefono', 'Pago a mi Novia', 'Pago Seguro de Carro']
row = 4
for egreso in egreso_labels:
    tk.Label(root, text=f"{egreso}:").grid(row=row, column=0, padx=5, pady=5)
    entrada = tk.Entry(root)
    entrada.grid(row=row, column=1, padx=5, pady=5)
    entry_egresos[egreso] = entrada
    row += 1

# Variables para mostrar resultados
resultado = tk.StringVar()
recomendacion = tk.StringVar()
resumen = tk.StringVar()

# Crear tabla para Ingresos
tree_ingresos = ttk.Treeview(root, columns=("Fecha", "Actividad", "Monto", "%"), show="headings")
tree_ingresos.heading("Fecha", text="Fecha")
tree_ingresos.heading("Actividad", text="Actividad")
tree_ingresos.heading("Monto", text="Monto")
tree_ingresos.heading("%", text="%")

tree_ingresos.grid(row=row, column=0, columnspan=2, padx=5, pady=5)

# Crear tabla para Egresos
tree_egresos = ttk.Treeview(root, columns=("Fecha", "Actividad", "Monto", "%"), show="headings")
tree_egresos.heading("Fecha", text="Fecha")
tree_egresos.heading("Actividad", text="Actividad")
tree_egresos.heading("Monto", text="Monto")
tree_egresos.heading("%", text="%")

tree_egresos.grid(row=row+1, column=0, columnspan=2, padx=5, pady=5)

# Botón para calcular los resultados
btn_calcular = tk.Button(root, text="Calcular", command=calcular)
btn_calcular.grid(row=row+2, column=0, columnspan=2, pady=10)
btn_resetear = tk.Button(root, text="Reset", command=lambda: [entry.delete(0, tk.END) for entry in entry_ingreso_semana + list(entry_egresos.values())])
btn_resetear.grid(row=row+2, column=2, columnspan=2, pady=10)

# Mostrar los resultados
tk.Label(root, textvariable=resultado).grid(row=row + 3, column=0, columnspan=2)
tk.Label(root, textvariable=recomendacion).grid(row=row + 4, column=0, columnspan=2)
tk.Label(root, textvariable=resumen).grid(row=row + 5, column=0, columnspan=2)

root.mainloop()
