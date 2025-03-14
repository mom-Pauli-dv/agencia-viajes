# database.py
import sqlite3
import bcrypt


def inicializar_db():
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    
    # Crear tablas
    cursor.execute('''CREATE TABLE IF NOT EXISTS destinos (
                        id_destino INTEGER PRIMARY KEY,
                        nombre_destino TEXT,
                        descripcion TEXT,
                        actividades_disponibles TEXT,
                        costo REAL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS paquetes (
                        id_paquete INTEGER PRIMARY KEY,
                        nombre TEXT,
                        descripcion TEXT,
                        fecha_inicio TEXT,
                        fecha_fin TEXT,
                        precio_total REAL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS reservas (
                        id_reserva INTEGER PRIMARY KEY,
                        id_paquete_turistico INTEGER,
                        id_cliente INTEGER,
                        fecha_reserva TEXT,
                        estado_reserva TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                        id_cliente INTEGER PRIMARY KEY,
                        nombre TEXT,
                        apellido TEXT,
                        mail TEXT,
                        contraseña TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id_usuario INTEGER PRIMARY KEY,
                        nombre TEXT,
                        email TEXT,
                        contraseña TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS administradores (
                        id_administrador INTEGER PRIMARY KEY,
                        id_usuario INTEGER,
                        FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario))''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    inicializar_db()  # Llama a la función para inicializar la base de datos

# Funciones CRUD para Destino
def agregar_destino(destino):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO destinos (nombre_destino, descripcion, actividades_disponibles, costo)
                      VALUES (?, ?, ?, ?)''', (destino.nombre_destino, destino.descripcion, destino.actividades_disponibles, destino.costo))
    conn.commit()
    conn.close()

def mostrar_destinos():
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM destinos')
    destinos = cursor.fetchall()
    conn.close()
    return destinos

def modificar_destino(id_destino, destino):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE destinos
                      SET nombre_destino = ?, descripcion = ?, actividades_disponibles = ?, costo = ?
                      WHERE id_destino = ?''', (destino.nombre_destino, destino.descripcion, destino.actividades_disponibles, destino.costo, id_destino))
    conn.commit()
    conn.close()

def eliminar_destino(id_destino):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM destinos WHERE id_destino = ?', (id_destino,))
    conn.commit()
    conn.close()

# Funciones CRUD para Paquete Turístico
def agregar_paquete(paquete):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO paquetes (nombre, descripcion, fecha_inicio, fecha_fin, precio_total)
                      VALUES (?, ?, ?, ?, ?)''', (paquete.nombre, paquete.descripcion, paquete.fecha_inicio, paquete.fecha_fin, paquete.precio_total))
    conn.commit()
    conn.close()

def mostrar_paquetes():
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM paquetes')
    paquetes = cursor.fetchall()
    conn.close()
    return paquetes

def modificar_paquete(id_paquete, paquete):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE paquetes
                      SET nombre = ?, descripcion = ?, fecha_inicio = ?, fecha_fin = ?, precio_total = ?
                      WHERE id_paquete = ?''', (paquete.nombre, paquete.descripcion, paquete.fecha_inicio, paquete.fecha_fin, paquete.precio_total, id_paquete))
    conn.commit()
    conn.close()

def eliminar_paquete(id_paquete):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM paquetes WHERE id_paquete = ?', (id_paquete,))
    conn.commit()
    conn.close()
    
def total_costo(id_paquete):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(costo) FROM destinos WHERE id_destino IN (SELECT id_destino FROM paquete_destinos WHERE id_paquete = ?)', (id_paquete,))
    total = cursor.fetchone()[0]
    conn.close()
    return total

# Funciones CRUD para Reserva
def agregar_reserva(reserva):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO reservas (id_paquete_turistico, id_cliente, fecha_reserva, estado_reserva)
                      VALUES (?, ?, ?, ?)''', (reserva.id_paquete_turistico, reserva.id_cliente, reserva.fecha_reserva, reserva.estado_reserva))
    conn.commit()
    conn.close()

def mostrar_reservas():
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM reservas')
    reservas = cursor.fetchall()
    conn.close()
    return reservas

def modificar_reserva(id_reserva, reserva):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE reservas
                      SET id_paquete_turistico = ?, id_cliente = ?, fecha_reserva = ?, estado_reserva = ?
                      WHERE id_reserva = ?''', (reserva.id_paquete_turistico, reserva.id_cliente, reserva.fecha_reserva, reserva.estado_reserva, id_reserva))
    conn.commit()
    conn.close()

def eliminar_reserva(id_reserva):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM reservas WHERE id_reserva = ?', (id_reserva,))
    conn.commit()
    conn.close()

# Funciones CRUD para Cliente
def agregar_cliente(cliente):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    contraseña_cifrada = bcrypt.hashpw(cliente.contraseña.encode('utf-8'), bcrypt.gensalt())
    cursor.execute('''INSERT INTO clientes (nombre, apellido, mail, contraseña)
                      VALUES (?, ?, ?, ?)''', (cliente.nombre, cliente.apellido, cliente.mail, contraseña_cifrada))
    conn.commit()
    conn.close()


def mostrar_clientes():
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    conn.close()
    return clientes

def modificar_cliente(id_cliente, cliente):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    contraseña_cifrada = bcrypt.hashpw(cliente.contraseña.encode('utf-8'), bcrypt.gensalt())
    cursor.execute('''UPDATE clientes
                      SET nombre = ?, apellido = ?, mail = ?, contraseña = ?
                      WHERE id_cliente = ?''', (cliente.nombre, cliente.apellido, cliente.mail, contraseña_cifrada, id_cliente))
    conn.commit()
    conn.close()

def eliminar_cliente(id_cliente):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM clientes WHERE id_cliente = ?', (id_cliente,))
    conn.commit()
    conn.close()
    
# Funciones CRUD para Usuario
def agregar_usuario(usuario):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    contraseña_cifrada = bcrypt.hashpw(usuario.contraseña.encode('utf-8'), bcrypt.gensalt())
    cursor.execute('''INSERT INTO usuarios (nombre, email, contraseña)
                      VALUES (?, ?, ?)''', (usuario.nombre, usuario.email, contraseña_cifrada))
    conn.commit()
    conn.close()

def mostrar_usuarios():
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

def modificar_usuario(id_usuario, usuario):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    contraseña_cifrada = bcrypt.hashpw(usuario.contraseña.encode('utf-8'), bcrypt.gensalt())
    cursor.execute('''UPDATE usuarios
                      SET nombre = ?, email = ?, contraseña = ?
                      WHERE id_usuario = ?''', (usuario.nombre, usuario.email, contraseña_cifrada, id_usuario))
    conn.commit()
    conn.close()

def eliminar_usuario(id_usuario):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id_usuario = ?', (id_usuario,))
    conn.commit()
    conn.close()

# Funciones CRUD para Administrador
def agregar_administrador(administrador):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO administradores (id_usuario)
                      VALUES (?)''', (administrador.id_usuario,))
    conn.commit()
    conn.close()

def mostrar_administradores():
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM administradores')
    administradores = cursor.fetchall()
    conn.close()
    return administradores

def eliminar_administrador(id_administrador):
    conn = sqlite3.connect('reservas.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM administradores WHERE id_administrador = ?', (id_administrador,))
    conn.commit()
    conn.close()
    
