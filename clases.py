# clases.py
# importaremos las excepciones personalizadas
from excepciones import ErrorDatos, ErrorServicio, ErrorReserva

# Clase Entidad
# Será la clase principal de nuestro codigo

from abc import ABC, abstractmethod

class Entidad(ABC): 
  
  @abstractmethod
  def mostrar_info(self):
    pass
# Clase Cliente
# Se encarga de de guardar el nombre y el documento de idenficación de cada uno de los clientes
class Cliente(Entidad):

    def __init__(self, nombre, documento):
        if not nombre or not documento:
            raise ErrorDatos("El nombre y documento son obligatorios")

        self.__nombre = nombre
        self.__documento = documento

    def mostrar_info(self):
        return f"Cliente: {self.__nombre} - Documento: {self.__documento}"

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

  # Clase servicio
  # Se encargará de definir los diferentes servicios que se ofrecen

class Servicio(ABC):

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def mostrar_descripcion(self):
        pass

# Reserva de salas
# Permite calcular el costo dependiendo de las horas en que vaya a utilizar la sala

class Reserva(Servicio):

    def calcular_costo(self, duracion):
        if duracion <= 0:
            raise ErrorServicio("La duración debe ser mayor que cero")

        return duracion * 20000

    def mostrar_descripcion(self):
        return "Reserva por horas"

# Alquiler de equipos
# Permite calcular el costo dependiendo de las horas en que vaya a alquilar el equipo

class AlquilerEquipo(Servicio):

    def calcular_costo(self, duracion):
        if duracion <= 0:
            raise ErrorServicio("La duración debe ser mayor que cero")

        return duracion * 15000

    def mostrar_descripcion(self):
        return "Alquiler de equipos por horas"

# Asesoríasespecializadas
# Permite calcular el costo dependiendo de las horas en que esten en la asesoría especializada

class Asesoríasespecializadas(Servicio):

    def calcular_costo(self, duracion):
        if duracion <= 0:
            raise ErrorServicio("La duración debe ser mayor que cero")

        return duracion * 30000

    def mostrar_descripcion(self):
        return "Servicio de asesoría especializadas por horas"

# CLASE RESERVA
# Relaciona al cliente con el servicio

class Reserva:

    def __init__(self, cliente, servicio, duracion):
        if not isinstance(cliente, Cliente):
            raise ErrorReserva("El cliente no es válido")

        if not isinstance(servicio, Servicio):
            raise ErrorReserva("El servicio no es válido")

        if duracion <= 0:
            raise ErrorReserva("La duración debe ser mayor que cero")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"
        return "Reserva confirmada correctamente"

    def cancelar(self):
        self.estado = "Cancelada"
        return "Reserva cancelada correctamente"

    def procesar(self):
        if self.estado != "Confirmada":
            raise ErrorReserva("Primero debe confirmar la reserva")

        costo = self.servicio.calcular_costo(self.duracion)

        return costo

    def __str__(self):
        return (
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.mostrar_descripcion()}\n"
            f"Duración: {self.duracion} horas\n"
            f"Estado: {self.estado}"
        )


      
