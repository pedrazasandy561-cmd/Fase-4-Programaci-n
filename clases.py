# clases.py
# importaremos las excepciones personalizadas
from excepciones import Errordatos, Errorservicio, Error reserva

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
      
