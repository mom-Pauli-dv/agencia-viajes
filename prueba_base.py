import dataBase

# Lista de funciones que deberían estar en dataBase
funciones_requeridas = [
    'agregar_destino', 'modificar_destino', 'eliminar_destino', 'mostrar_destinos',
    'agregar_paquete', 'modificar_paquete', 'eliminar_paquete', 'mostrar_paquetes',
    'agregar_reserva', 'modificar_reserva', 'eliminar_reserva', 'mostrar_reservas',
    'agregar_cliente', 'modificar_cliente', 'eliminar_cliente', 'mostrar_clientes',
    'iniciar_sesion', 'agregar_usuario', 'modificar_usuario', 'eliminar_usuario',
    'mostrar_usuarios', 'agregar_administrador'
]

for funcion in funciones_requeridas:
    if hasattr(dataBase, funcion):
        print(f"La función {funcion} está disponible.")
    else:
        print(f"Falta la función {funcion}.")