import pandas as pd
from collections import Counter

# Dataset ampliado
data = {
    "usuario": ["Luis", "Luis", "Ana", "Ana", "Ana", "Carla", "Carla", "Pedro"],
    "producto": ["Laptop", "Mouse", "Laptop", "Audífonos", "Mouse", "Mouse", "Laptop", "Audífonos"]
}

df = pd.DataFrame(data)

def recomendar(usuario, top=3):
    # Productos del usuario actual
    productos_usuario = set(df[df["usuario"] == usuario]["producto"])

    # Usuarios similares (que comparten al menos 1 producto)
    usuarios_similares = df[df["producto"].isin(productos_usuario)]["usuario"].unique()

    # Productos de usuarios similares
    productos_similares = df[df["usuario"].isin(usuarios_similares)]["producto"]

    # Contar popularidad
    conteo = Counter(productos_similares)

    # Eliminar productos que el usuario ya tiene
    for p in productos_usuario:
        if p in conteo:
            del conteo[p]

    # Retornar los más frecuentes
    recomendados = [p for p, _ in conteo.most_common(top)]
    return recomendados

print("Recomendaciones para Luis:", recomendar("Luis"))
print("Recomendaciones para Ana:", recomendar("Ana"))
print("Recomendaciones para Carla:", recomendar("Carla"))
print("Recomendaciones para Pedro:", recomendar("Pedro"))
