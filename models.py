# models.py
from dataBase import agregar_destino, modificar_destino, eliminar_destino, mostrar_destinos
from dataBase import agregar_paquete, modificar_paquete, eliminar_paquete, mostrar_paquetes
from dataBase import agregar_reserva, modificar_reserva, eliminar_reserva, mostrar_reservas
from dataBase import agregar_cliente, modificar_cliente, eliminar_cliente, mostrar_clientes
from dataBase import agregar_usuario, modificar_usuario, eliminar_usuario, mostrar_usuarios
from dataBase import agregar_administrador
from auth import iniciar_sesion as db_iniciar_sesion
from dataBase import inicializar_db


class Destino:
    def __init__(self, id_destino, nombre_destino, descripcion, actividades_disponibles, costo):
        self.id_destino = id_destino
        self.nombre_destino = nombre_destino
        self.descripcion = descripcion
        self.actividades_disponibles = actividades_disponibles
        self.costo = costo

    def agregarDestino(self):
        agregar_destino(self)

    def mostrarDestino(self):
        return mostrar_destinos(self.id_destino)
        

    def modificarDestino(self):
        modificar_destino(self.id_destino, self)

    def eliminarDestino(self):
        eliminar_destino(self.id_destino)
    
class PaqueteTuristico:
    def __init__(self, id_paquete, nombre, descripcion, fecha_inicio, fecha_fin, precio_total):
        self.id_paquete = id_paquete
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.precio_total = precio_total

    def agregar_paquete(self):
        agregar_paquete(self)

    def mostrar_paquete(self):
        return mostrar_paquetes

    def modificar_paquete(self):
        modificar_paquete(self.id_paquete, self)

    def eliminar_paquete(self):
        eliminar_paquete(self.id_paquete)

    def calcular_precio(self):
        # Lógica para calcular el precio total del paquete turístico
        pass


class Reserva:
    def __init__(self, id_reserva, id_paquete_turistico, id_cliente, fecha_reserva, estado_reserva):
        self.id_reserva = id_reserva
        self.id_paquete_turistico = id_paquete_turistico
        self.id_cliente = id_cliente
        self.fecha_reserva = fecha_reserva
        self.estado_reserva = estado_reserva

    def realizar_reserva(self):
        agregar_reserva(self)

    def mostrar_reserva(self):
        return mostrar_reservas()

    def modificar_reserva(self):
        modificar_reserva(self.id_reserva)

    def eliminar_reserva(self):
        eliminar_reserva(self.id_reserva)


class Usuario:
    def __init__(self, id_usuario, nombre, email, contraseña):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña

    def iniciar_sesion(self):
        return db_iniciar_sesion(self.email, self.contraseña)

    def modificar_perfil(self):
        modificar_usuario(self.id_usuario, self)


class Cliente:
    def __init__(self, id_cliente, nombre, apellido, mail, contraseña, reservas=None):
        if reservas is None:
            reservas = []
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.contraseña = contraseña
        self.reservas = reservas

    def registrar_cliente(self):
        agregar_cliente(self)

    def iniciar_sesion(self):
        return db_iniciar_sesion(self.mail, self.contraseña)

    def mostrar_perfil(self):
        return mostrar_clientes

    def modificar_perfil(self):
        modificar_cliente(self.id_cliente, self)

    def ver_reservas(self):
        return mostrar_reservas()



class Administrador(Usuario):
    def __init__(self, id_usuario, nombre, email, contraseña):
        super().__init__(id_usuario, nombre, email, contraseña)

    def agregar_destino(self):
        agregar_destino(self)

    def agregar_paquete(self):
        agregar_paquete(self)

    def gestionar_reservas(self):
       return mostrar_reservas()


if __name__ == "__main__":
    # Inicializar la base de datos
    inicializar_db()

    # Prueba de importación
    print("Prueba de importación:")
    print(agregar_usuario)  # Debería mostrar la referencia a la función
    print(eliminar_cliente)  # Debería mostrar la referencia a la función
    print(eliminar_usuario)  # Debería mostrar la referencia a la función
    print(mostrar_usuarios)  # Debería mostrar la referencia a la función
    print(agregar_administrador)  # Debería mostrar la referencia a la función

    # Ejemplo de uso: agregar un nuevo destino
    nuevo_destino = Destino(None, "Montañas Rocosas", "Un hermoso destino de montaña", "Senderismo, Escalada", 200.0)
    nuevo_destino.agregarDestino()  # Agregar un nuevo destino a la base de datos

    # Mostrar todos los destinos
    destinos = mostrar_destinos()
    print("Destinos disponibles:", destinos)