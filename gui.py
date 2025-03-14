# gui.py
import tkinter as tk
from tkinter import messagebox, simpledialog
from auth import iniciar_sesion  # Asegúrate de que esta función esté definida en auth.py

def iniciar_gui():
    root = tk.Tk()
    root.title("Sistema de Reservas de Paquetes Turísticos")

    # Crear un marco para el formulario de inicio de sesión
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Etiquetas y campos de entrada
    tk.Label(frame, text="Email:").grid(row=0, column=0, padx=5, pady=5)
    email_entry = tk.Entry(frame)
    email_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5)
    password_entry = tk.Entry(frame, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    # Función para manejar el inicio de sesión
    def login():
        email = email_entry.get()
        contraseña = password_entry.get()
        if iniciar_sesion(email, contraseña):
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
            # Aquí puedes abrir otra ventana o realizar otras acciones
        else:
            messagebox.showerror("Error", "Email o contraseña incorrectos")

    # Botón de inicio de sesión
    login_button = tk.Button(frame, text="Iniciar Sesión", command=login)
    login_button.grid(row=2, columnspan=2, pady=10)

    # Iniciar el bucle principal de la GUI
    root.mainloop()

if __name__ == "__main__":
    iniciar_gui()