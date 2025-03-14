# main.py
from gui import iniciar_gui
from dataBase import inicializar_db
from auth import iniciar_sesion
from utils import validar_email

def main():
    # Inicializar la base de datos
    inicializar_db()
    
    #solicita email y contraseña
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")
    
    #valida email
    if not validar_email(email):
        print("Email no válido.")
        return  # Salir si el email no es válido
    
    #inicia sesion
    if iniciar_sesion(email, contraseña):
        print("Inicio de sesión exitoso")
        #inicia la interfaz grafica
        iniciar_gui()
    else:
        print("Email o contraseña incorrectos")

if __name__ == "__main__":
    main()

    
