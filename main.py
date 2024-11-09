class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if(color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco"):
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo


class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        cantidad = 0
        for i in self.asientos:
            if type(i) is Asiento:
                cantidad += 1

    def verificarIntegridad(self):
        rMotor = self.motor.registro
        rAuto = self.registro
        iguales = True
        original = ""

        for i in self.asientos:
            if i != None and i.registro == rAuto:
                iguales = False
                break

        if rMotor == rAuto and iguales:
            original = "Auto original"
        else:
            original = "Las piezas no son originales"

        return original