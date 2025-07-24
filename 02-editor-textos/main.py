import tkinter as tk
from tkinter import filedialog, messagebox


class EditorTexto:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto")
        self.ruta_archivo = None

        # Área de texto con scroll
        self.texto = tk.Text(root, wrap="word", undo=True)
        self.texto.pack(expand=True, fill="both")

        scroll = tk.Scrollbar(self.texto, command=self.texto.yview)
        scroll.pack(side="right", fill="y")
        self.texto.config(yscrollcommand=scroll.set)

        # Menú superior
        self.crear_menus()

        # Menú contextual (clic derecho)
        self.crear_menu_contextual()
        self.texto.bind("<Button-3>", self.mostrar_menu_contextual)  # Clic derecho Windows/Linux
        self.texto.bind("<Button-2>", self.mostrar_menu_contextual)  # Clic derecho en macOS

    def crear_menus(self):
        menubar = tk.Menu(self.root)

        archivo_menu = tk.Menu(menubar, tearoff=0)
        archivo_menu.add_command(label="Abrir", command=self.abrir_archivo)
        archivo_menu.add_command(label="Guardar", command=self.guardar_archivo)
        archivo_menu.add_command(label="Guardar como...", command=self.guardar_como)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.root.quit)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)

        edicion_menu = tk.Menu(menubar, tearoff=0)
        edicion_menu.add_command(label="Cortar", command=lambda: self.texto.event_generate("<<Cut>>"))
        edicion_menu.add_command(label="Copiar", command=lambda: self.texto.event_generate("<<Copy>>"))
        edicion_menu.add_command(label="Pegar", command=lambda: self.texto.event_generate("<<Paste>>"))
        edicion_menu.add_separator()
        edicion_menu.add_command(label="Deshacer", command=lambda: self.texto.event_generate("<<Undo>>"))
        edicion_menu.add_command(label="Rehacer", command=lambda: self.texto.event_generate("<<Redo>>"))
        edicion_menu.add_separator()
        edicion_menu.add_command(label="Seleccionar todo", command=lambda: self.texto.event_generate("<<SelectAll>>"))
        menubar.add_cascade(label="Edición", menu=edicion_menu)

        self.root.config(menu=menubar)

    def crear_menu_contextual(self):
        self.menu_contextual = tk.Menu(self.root, tearoff=0)
        self.menu_contextual.add_command(label="Cortar", command=lambda: self.texto.event_generate("<<Cut>>"))
        self.menu_contextual.add_command(label="Copiar", command=lambda: self.texto.event_generate("<<Copy>>"))
        self.menu_contextual.add_command(label="Pegar", command=lambda: self.texto.event_generate("<<Paste>>"))
        self.menu_contextual.add_separator()
        self.menu_contextual.add_command(label="Seleccionar todo", command=lambda: self.texto.event_generate("<<SelectAll>>"))

    def mostrar_menu_contextual(self, event):
        try:
            self.menu_contextual.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu_contextual.grab_release()

    def abrir_archivo(self):
        ruta = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if ruta:
            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    contenido = f.read()
                self.texto.delete(1.0, tk.END)
                self.texto.insert(tk.END, contenido)
                self.ruta_archivo = ruta
                self.root.title(f"Editor de Texto - {ruta}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{e}")

    def guardar_archivo(self):
        if self.ruta_archivo:
            try:
                with open(self.ruta_archivo, "w", encoding="utf-8") as f:
                    f.write(self.texto.get(1.0, tk.END))
                messagebox.showinfo("Guardado", "Archivo guardado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")
        else:
            self.guardar_como()

    def guardar_como(self):
        ruta = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if ruta:
            try:
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(self.texto.get(1.0, tk.END))
                self.ruta_archivo = ruta
                self.root.title(f"Editor de Texto - {ruta}")
                messagebox.showinfo("Guardado", "Archivo guardado correctamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = EditorTexto(root)
    root.mainloop()
