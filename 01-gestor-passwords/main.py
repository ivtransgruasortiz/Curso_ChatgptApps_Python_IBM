import tkinter as tk
from tkinter import messagebox
import random
import string

def generar_contraseña():
    try:
        longitud = int(entry_longitud.get())
        if longitud <= 0:
            raise ValueError("La longitud debe ser mayor que cero.")

        caracteres = string.ascii_letters + string.digits + string.punctuation
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, contraseña)
    except ValueError as e:
        messagebox.showerror("Error", f"Entrada no válida: {e}")

def copy_resultado():
    ventana.clipboard_clear()
    ventana.clipboard_append(entry_resultado.get())
    ventana.update()
    messagebox.showinfo("Copiado", "La contraseña ha sido copiada al portapapeles.")

def show_context_menu(event):
    menu_contextual.post(event.x_root, event.y_root)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("400x200")
ventana.resizable(False, False)

# Etiqueta para la longitud
label_longitud = tk.Label(ventana, text="Longitud de la contraseña:")
label_longitud.pack(pady=10)

# Entrada para la longitud
entry_longitud = tk.Entry(ventana, justify="center")
entry_longitud.pack()

# Botón para generar la contraseña
btn_generar = tk.Button(ventana, text="Generar", command=generar_contraseña)
btn_generar.pack(pady=10)

# Entrada para mostrar la contraseña generada
entry_resultado = tk.Entry(ventana, width=40, justify="center")
entry_resultado.pack(pady=10)

# Crear un menu contextual
menu_contextual = tk.Menu(ventana, tearoff=0)
menu_contextual.add_command(label="Copiar", command=copy_resultado)
ventana.bind("<Button-3>", show_context_menu)

# Ejecutar la aplicación
ventana.mainloop()