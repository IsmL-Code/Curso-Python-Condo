from typing import Dict, List

# Diccionario de estudiantes y sus materias
estudiantes_materias: Dict[str, List[str]] = {
    'Daniel': ['Matematica', 'Computacion'],
    'Maria': ['Matematica', 'Fisica'],
    'Jefferson': ['Programacion Web', 'POO'],
    'Ismael': ['Programacion Web', 'Inteligencia Artificial']
}

def devolver_materias(nombre: str) -> List[str]:
    
    try:
        return estudiantes_materias[nombre]
    except KeyError:
        raise KeyError(f"El estudiante '{nombre}' no está registrado.")
