<<<<<<< HEAD
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

=======
def ver_resultados(votos: dict):
    """
    Muestra el total de votos y el porcentaje correspondiente a cada opción.
    Recibe un diccionario con el formato: {"Candidato A": 10, "Candidato B": 5}
    """
    total_votos = sum(votos.values())
    
    print("\n--- RESULTADOS DE LA VOTACIÓN ---")
    
    if total_votos == 0:
        print("Aún no se han registrado votos.")
        return

    for opcion, cantidad in votos.items():
        porcentaje = (cantidad / total_votos) * 100
        print(f"{opcion}: {cantidad} votos ({porcentaje:.2f}%)")
        
    print(f"Total de votos emitidos: {total_votos}\n")

# Ejemplo de uso para probar la función:
if __name__ == "__main__":
    conteo_ejemplo = {
        "Opción A": 15,
        "Opción B": 25,
        "Voto en Blanco": 10
    }
    ver_resultados(conteo_ejemplo)
>>>>>>> feature/ver-resultados
