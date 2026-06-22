import utilities #import de las utilidades


class Student:#crear la clase student
    def __init__(self, name, classroom , spanish_grade, english_grade, history_grade, science_grade ):#definir el constructor de los estudiantes
        self.name = name
        self.classroom = classroom
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.history_grade = history_grade
        self.science_grade= science_grade
        self.promedio = ((int(spanish_grade) + int(english_grade) + int(history_grade) + int(science_grade))/4)


    def show_student_info(self):
        print(f"\nNombre: {self.name} \nSeccion: {self.classroom} \nEspañol: {self.spanish_grade} \nIngles: {self.english_grade} \nSociales: {self.history_grade} \nCiencias: {self.science_grade} \nPromedio {self.promedio}" )

    def show_studnet_average(self):
        print(f"\nNombre: {self.name} \nPromedio {self.promedio}" )

    def get_promedio(self):
        return self.promedio
    
    def create_directory(self):
        return{ #diccionario para crear un nuevo estudiante
            "Nombre" : self.name,
            "Seccion" : self.classroom,
            "Espanol" : self.spanish_grade,
            "Ingles" : self.english_grade,
            "Sociales" : self.history_grade,
            "Ciencias" : self.science_grade,
            "Promedio" : self.promedio #calculo del promedio del estudiante 
        }
        