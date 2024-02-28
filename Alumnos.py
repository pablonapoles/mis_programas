class Estudiante:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.calificaciones = []
        self.asistencias = []

    def agregar_calificacion(self, calificacion):
        if 0 <= calificacion <= 5:
            self.calificaciones.append(calificacion)
        else:
            print("La calificación debe estar en el rango de 0 a 5.")

    def agregar_asistencia(self, asistencia):
        if 0 <= asistencia <= 100:
            self.asistencias.append(asistencia)
        else:
            print("El porcentaje de asistencia debe estar en el rango de 0 a 100.")

    def promedio_calificaciones(self):
        return sum(self.calificaciones) / len(self.calificaciones) if self.calificaciones else 0

    def promedio_asistencias(self):
        return sum(self.asistencias) / len(self.asistencias) if self.asistencias else 0

    def evaluar(self):
        promedio_calificaciones = self.promedio_calificaciones()
        promedio_asistencias = self.promedio_asistencias()

        if promedio_calificaciones >= 3 and promedio_asistencias >= 80:
            return "Aprobado"
        else:
            return "Reprobado"

    def sugerir_plan_de_accion(self):
        promedio_calificaciones = self.promedio_calificaciones()
        promedio_asistencias = self.promedio_asistencias()

        acciones = []

        if promedio_calificaciones < 3:
            acciones.append("mejorar sus calificaciones")
        if promedio_asistencias < 80:
            acciones.append("mejorar su asistencia")

        if acciones:
            return f"El estudiante {self.nombre} {self.apellido} necesita {', '.join(acciones)}."
        else:
            return f"El estudiante {self.nombre} {self.apellido} está en buen camino."

    def __str__(self):
        return f"{self.nombre} {self.apellido}: Promedio de calificaciones: {self.promedio_calificaciones()}, Promedio de asistencias: {self.promedio_asistencias()}%, Estado: {self.evaluar()}"


def registrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    estudiante = Estudiante(nombre, apellido)
    cantidad_notas = int(input(f"Ingrese la cantidad de notas para {nombre} {apellido}: "))
    for _ in range(cantidad_notas):
        calificacion = float(input("Ingrese la nota del estudiante (del 0 al 5): "))
        estudiante.agregar_calificacion(calificacion)
    cantidad_asistencias = int(input(f"Ingrese el porcentaje de asistencias para {nombre} {apellido}: "))
    estudiante.agregar_asistencia(cantidad_asistencias)
    return estudiante


def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("\nDatos de los estudiantes:")
        for estudiante in estudiantes:
            print(estudiante)


def sugerir_plan_accion(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("Planes de acción sugeridos:")
        for estudiante in estudiantes:
            print(estudiante.sugerir_plan_de_accion())

def menu():
    print("\n1. Registrar estudiante")
    print("2. Mostrar datos de estudiantes")
    print("3. Sugerir plan de acción para estudiantes")
    print("4. Salir")

estudiantes = []

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        estudiante = registrar_estudiante()
        estudiantes.append(estudiante)
        print("Estudiante registrado exitosamente.")
    elif opcion == "2":
        mostrar_estudiantes(estudiantes)
    elif opcion == "3":
        sugerir_plan_accion(estudiantes)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
