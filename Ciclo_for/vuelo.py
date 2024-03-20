vuelo = {
    "Aerolinea": "Avianca",
    "Vuelo": "AV3102",
    "Origen": "CTG",
    "Destino": "MDE",
    "Tipo_Maleta": ['Cabina', 'Mano', 'Bodega']
}

print("Imprimir valores del diccionario:")
for key, value in vuelo.items():
    print(f"{key}: {value}")

print("\nImprimir Valores del tipo de maleta:")
[print(maleta) for maleta in vuelo["Tipo_Maleta"]]



