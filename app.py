import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora con TKINTER")
root.geometry("400x500")  # Establecer un tamaño fijo para la ventana más grande
root.configure(bg='#2E2E2E')  # Fondo oscuro para la ventana

# Crear la pantalla de la calculadora
pantalla = tk.Entry(root, width=20, borderwidth=2, relief="ridge", bg='#1E1E1E', fg='white', font=('Arial', 32), justify='right')  # Aumentar tamaño de fuente
pantalla.grid(row=0, column=0, columnspan=4, padx=15, pady=15)  # Ajustar margen para mayor tamaño

# Función para actualizar la pantalla
def click_boton(valor):
    actual = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, actual + valor)

#Función para evaluar la expresión
def evaluar():
    try:
       resultado=eval(pantalla.get())
       #Borra todo el contenido del widget
       pantalla.delete(0,tk.END)
       #Inserta el resultado evaluado
       pantalla.insert(0,resultado)
    except Exception as e:
        pantalla.delete(0, tk.END)
        #Nos muestra el texto "ERROR" si algo salió mal
        pantalla.insert(0,"Error")

#Función para borrar pantalla
def borrar():
    pantalla.delete(0,tk.END)