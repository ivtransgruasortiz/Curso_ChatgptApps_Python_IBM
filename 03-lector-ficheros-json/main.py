import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
import json
import os

ARCHIVO_JSON = "productos.json"  # Asegúrate de que este archivo existe en la misma carpeta

class TablaProductos:
    def __init__(self, root):
        self.root = root
        self.root.title("Productos en Inventario")
        self.root.geometry("700x400")

        columnas = ("ID", "NOMBRE", "DESCRIPCION", "PRECIO")
        self.tabla = ttk.Treeview(root, columns=columnas, show="headings")

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=150)

        self.tabla.pack(expand=True, fill="both", padx=10, pady=10)

        self.cargar_datos()

        # Doble clic en una fila
        self.tabla.bind("<Double-1>", self.mostrar_resumen_producto)

    def cargar_datos(self):
        if not os.path.exists(ARCHIVO_JSON):
            messagebox.showerror("Error", f"No se encontró el archivo: {ARCHIVO_JSON}")
            return

        try:
            with open(ARCHIVO_JSON, "r", encoding="utf-8") as f:
                self.productos = json.load(f)

            for producto in self.productos:
                self.tabla.insert("", "end", values=(
                    producto.get("ID"),
                    producto.get("NOMBRE"),
                    producto.get("DESCRIPCION"),
                    f"{producto.get('PRECIO'):.2f} €"
                ))

        except json.JSONDecodeError:
            messagebox.showerror("Error", "El archivo JSON tiene un formato inválido.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo JSON:\n{e}")

    def mostrar_resumen_producto(self, event):
        item = self.tabla.focus()
        if not item:
            return

        valores = self.tabla.item(item, "values")
        if not valores:
            return

        # Extraemos nombre, descripción y precio (ID está en valores[0], que no usamos)
        nombre = valores[1]
        descripcion = valores[2]
        precio = valores[3]

        resumen = Toplevel(self.root)
        resumen.title("Resumen del Producto")
        resumen.geometry("400x180")

        ttk.Label(resumen, text="🛍 Producto Seleccionado", font=("Arial", 12, "bold")).pack(pady=10)

        ttk.Label(resumen, text=f"Nombre: {nombre}", font=("Arial", 11)).pack(pady=5)
        ttk.Label(resumen, text=f"Descripción: {descripcion}", font=("Arial", 11)).pack(pady=5)
        ttk.Label(resumen, text=f"Precio: {precio}", font=("Arial", 11)).pack(pady=5)

        ttk.Button(resumen, text="Cerrar", command=resumen.destroy).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = TablaProductos(root)
    root.mainloop()

