# Diccionario para guardar las personas que ya votaron
votantes = {}

while True:
    documento = input("Ingrese el número de documento (o 'salir' para terminar): ")

    if documento.lower() == "salir":
        break

    # Verificar si la persona ya votó
    if documento in votantes:
        print(" Esta persona ya votó. No puede votar nuevamente.")
    else:
        voto = input("Ingrese su voto: ")

        # Guardar la persona y su voto en el diccionario
        votantes[documento] = voto

        print("✅ Voto registrado correctamente.")

print("\nVotantes registrados:")
print(votantes)

