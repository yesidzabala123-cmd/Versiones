votos = {}

def reiniciar_votacion():
    with open("historial.txt", "a") as archivo:
        archivo.write(str(votos) + "\n")
    votos.clear()
    print("Votación reiniciada.")



reiniciar_votacion()