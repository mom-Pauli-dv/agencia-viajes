# auth.py
import sqlite3
import bcrypt



def verificar_contraseña(contraseña, contraseña_cifrada):
    return bcrypt.checkpw(contraseña.encode('utf-8'), contraseña_cifrada)

def iniciar_sesion(email, contraseña):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT contraseña FROM usuarios WHERE email = ?', (email,))
    resultado = cursor.fetchone()
    conn.close()
    
    if resultado:
        contraseña_cifrada = resultado[0]
        if verificar_contraseña(contraseña, contraseña_cifrada):
            return True
        else:
            return False
    else:
        return False