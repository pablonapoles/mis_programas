import re
from pyswip import Prolog

class DiagnosticoColera:
    def __init__(self):
        self.prolog = Prolog()
        self.prolog.consult("c:/Users/pablo/Documents/VSC/Prolog/colera2.pl")

    def solicitar_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje))
            except ValueError:
                print("Por favor, ingresa un número válido.")

    def validar_nombre(self, nombre):
        return bool(re.match(r'^[a-zA-Z\s]+$', nombre))

    def solicitar_nombre(self, i):
        while True:
            nombre = input(f"Por favor, ingresa el nombre del paciente {i}: ").lower()
            if self.validar_nombre(nombre):
                return nombre
            print("Por favor, ingresa un nombre válido (solo letras y espacios).")

    def ejecutar_diagnostico(self):
        num_pacientes = self.solicitar_entero("Por favor, ingresa el número de pacientes a diagnosticar: ")
        pacientes = [self.solicitar_nombre(i+1) for i in range(num_pacientes)]

        for paciente in pacientes:
            consulta = f"diagnostico('{paciente}')."
            for _ in self.prolog.query(consulta):
                print(f"\nDiagnóstico para {paciente}:")

# Utlizacion
if __name__ == "__main__":
    diagnostico = DiagnosticoColera()
    diagnostico.ejecutar_diagnostico()
