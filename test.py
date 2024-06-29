import functions as fn

# Función para convertir grados a radianes
def toRadians(degrees: float) -> float:
    return degrees * (math.pi / 180)

# Función para convertir radianes a grados
def toDegrees(radians: float) -> float:
    return radians * (180 / math.pi)

# Función para convertir grados a grados-minutos-segundos (DMS)
def toDMS(degrees: float) -> tuple:
    deg = int(degrees)
    minutes_float = (degrees - deg) * 60
    minutes = int(minutes_float)
    seconds = (minutes_float - minutes) * 60
    return deg, minutes, seconds

# Función para convertir grados-minutos-segundos (DMS) a grados decimales
def fromDMS(degrees, minutes, seconds) -> float:
    return degrees + (minutes / 60) + (seconds / 3600)

# Ejemplo de uso
degrees = 45
radians = toRadians(degrees)
dms = toDMS(degrees)
degrees_from_dms = fromDMS(*dms)

print()

print(f"{degrees} grados son {radians} radianes.")
print(f"{degrees} grados son {dms[0]}° {dms[1]}' {dms[2]:.2f}\".")
print(f"Conversión de grados-minutos-segundos a grados decimales: {degrees_from_dms} grados.")