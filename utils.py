# utils.py
import re

def validar_email(email):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, email) is not None

def formatear_fecha(fecha):
    """Formatea una fecha a un formato legible."""
    return fecha.strftime("%d/%m/%Y")  # Ejemplo de formato

def calcular_precio_total(paquete):
    """Calcula el precio total de un paquete turístico."""
    # Aquí puedes implementar la lógica para calcular el precio total
    return paquete.precio_total 