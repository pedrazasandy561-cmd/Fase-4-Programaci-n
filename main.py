
# main.py

# Importamos las clases que creamos en clases.py
from clases import (
    Cliente,
    ReservaSala,
    AlquilerEquipo,
    Asesoriasespecializadas
)

# Importamos las excepciones personalizadas
from excepciones import ErrorDatos, ErrorReserva, ErrorCliente

# Importamos logging para guardar los errores
import logging


# Configuramos el registro de errores
logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Función para comprobar que los resultados sean correctos
def comprobar(resultado, esperado):

    if resultado != esperado:
        raise AssertionError("El resultado no es el esperado")


# Función para comprobar los errores esperados
def esperar_error(tipo_error, funcion):

    try:
        funcion()
        raise AssertionError("No se presentó el error esperado")

    except tipo_error:
        pass


# Función para ejecutar las 10 pruebas que nos permitirán comprobar la creación de clientes, su información, la reserva, el costo, la cancelación o confirmación de la reserva
def ejecutar_prueba(numero, descripcion, funcion):

    try:
        funcion()
        print(f"Prueba {numero}: {descripcion} - APROBADA")

    except Exception as error:
        print(f"Prueba {numero}: {descripcion} - FALLIDA")
        logging.exception(f"Error en la prueba {numero}: {error}")


# Creamos un cliente y los servicios
cliente = Cliente("Adriana Pedraza", "1070986401")

sala = ReservaSala()
equipo = AlquilerEquipo()
asesoria = Asesoriasespecializadas()


# INICIO DE LAS PRUEBAS
print("\n===== PRUEBAS DEL SISTEMA =====\n")


# PRUEBA 1: Crear un cliente
ejecutar_prueba(
    1,
    "Crear cliente",
    lambda: Cliente("Martha Beltran", "5197890")
)


# PRUEBA 2: Mostrar información del cliente
ejecutar_prueba(
    2,
    "Mostrar información del cliente",
    lambda: comprobar(
        cliente.mostrar_info(),
        "Cliente: Adriana Pedraza - Documento: 1070986401"
    )
)


# PRUEBA 3: Calcular costo de reserva de sala
ejecutar_prueba(
    3,
    "Calcular costo de reserva de sala",
    lambda: comprobar(sala.calcular_costo(2), 40000)
)


# PRUEBA 4: Calcular costo de alquiler de equipos
ejecutar_prueba(
    4,
    "Calcular costo de alquiler de equipos",
    lambda: comprobar(equipo.calcular_costo(2), 30000)
)


# PRUEBA 5: Calcular costo de asesorías especializadas
ejecutar_prueba(
    5,
    "Calcular costo de asesoría",
    lambda: comprobar(asesoria.calcular_costo(2), 60000)
)


# PRUEBA 6: Confirmar una reserva
reserva = Reserva(cliente, sala, 2)

ejecutar_prueba(
    6,
    "Confirmar reserva",
    lambda: comprobar(
        reserva.confirmar(),
        "Reserva confirmada correctamente"
    )
)


# PRUEBA 7: Procesar una reserva
ejecutar_prueba(
    7,
    "Procesar reserva",
    lambda: comprobar(reserva.procesar(), 40000)
)


# PRUEBA 8: Cancelar una reserva
reserva_cancelada = Reserva(cliente, equipo, 1)

ejecutar_prueba(
    8,
    "Cancelar reserva",
    lambda: comprobar(
        reserva_cancelada.cancelar(),
        "Reserva cancelada correctamente"
    )
)


# PRUEBA 9: Comprobar datos incorrectos
ejecutar_prueba(
    9,
    "Controlar datos incorrectos",
    lambda: esperar_error(
        ErrorDatos,
        lambda: Cliente("", "")
    )
)


# PRUEBA 10: Comprobar duración incorrecta
ejecutar_prueba(
    10,
    "Controlar duración incorrecta",
    lambda: esperar_error(
        ErrorReserva,
        lambda: Reserva(cliente, sala, 0)
    )
)


# Finalización de las pruebas
print("\n===== FIN DE LAS PRUEBAS =====")

      
