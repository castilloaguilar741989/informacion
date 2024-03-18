informacion_personal = {
    "nombre": "Jenny Castillo",
    "edad": 35,
    "ciudad": "Quito",
    "profesion": "Estudiante"
}

# Acceder y Modificar Valores
informacion_personal["ciudad"] = "Guayaquil"  # Modificar la ciudad a Guayaquil
informacion_personal["profesion"] = "Doctora"  # Agregar la profesión como Doctor

# Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0991234567"  # Agregar teléfono ficticio

# Eliminar una Clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminar la clave edad

# Imprimir el Diccionario Final
print(informacion_personal)
