from typing import List
from instituto.estudiantes import devolver_materias

def estudiante_registrado_en_materia(nombre: str, materia: str) -> bool:
   
    try:
        materias = devolver_materias(nombre)
        return materia in materias
    except KeyError:
        print(f"Error: El estudiante '{nombre}' no está registrado.")
        return False
