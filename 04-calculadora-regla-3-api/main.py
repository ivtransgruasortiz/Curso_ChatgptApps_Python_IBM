import tkinter as tk
from tkinter import messagebox

class ReglaDeTresApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Regla de Tres")
        self.root.geometry("400x250")  # Tamaño inicial un poco más grande
        self.root.resizable(True, True)  # Permitir ajustar tamaño

        self.font_label = ("Arial", 12)
        self.font_entry = ("Arial", 12)
        self.font_button = ("Arial", 12, "bold")
        self.font_result = ("Arial", 12, "bold")

        self.resultado_var = tk.StringVar()
        self.resultado_var.set("Introduce valores y pulsa Calcular")

        self._crear_widgets()

    def _crear_widgets(self):
        tk.Label(self.root, text="A", font=self.font_label).grid(row=0, column=0, padx=10, pady=8, sticky="w")
        tk.Label(self.root, text="B", font=self.font_label).grid(row=1, column=0, padx=10, pady=8, sticky="w")
        tk.Label(self.root, text="C", font=self.font_label).grid(row=2, column=0, padx=10, pady=8, sticky="w")

        self.entry_a = tk.Entry(self.root, font=self.font_entry)
        self.entry_b = tk.Entry(self.root, font=self.font_entry)
        self.entry_c = tk.Entry(self.root, font=self.font_entry)

        self.entry_a.grid(row=0, column=1, padx=10, pady=8, sticky="ew")
        self.entry_b.grid(row=1, column=1, padx=10, pady=8, sticky="ew")
        self.entry_c.grid(row=2, column=1, padx=10, pady=8, sticky="ew")

        btn_calcular = tk.Button(
            self.root,
            text="Calcular",
            font=self.font_button,
            bg="#1E90FF",    # DodgerBlue
            fg="white",
            activebackground="#104E8B",
            activeforeground="white",
            command=self.calcular
        )
        # Botón sin sticky para que no ocupe toda la fila
        btn_calcular.grid(row=3, column=0, columnspan=2, pady=15, ipadx=20, ipady=8)

        self.label_resultado = tk.Label(self.root, textvariable=self.resultado_var, font=self.font_result)
        self.label_resultado.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

        # Configurar columnas para que crezcan con la ventana
        self.root.grid_columnconfigure(1, weight=1)

    def calcular(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            c = float(self.entry_c.get())

            if a == 0:
                raise ZeroDivisionError("El valor de A no puede ser cero.")

            resultado = (b * c) / a
            self.resultado_var.set(f"Resultado: {resultado:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Introduce solo números válidos.")
        except ZeroDivisionError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ReglaDeTresApp(root)
    root.mainloop()
