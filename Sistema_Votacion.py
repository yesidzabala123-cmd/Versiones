votos = {}

def reiniciar_votacion():
    with open("historial.txt", "a") as archivo:
        for persona, candidato in votos.items():
            archivo.write(candidato + "\n")

    votos.clear()
    print("Votación reiniciada.")

def ganador():
    conteo = {}

    with open("historial.txt", "r") as archivo:
        for candidato in archivo:
            candidato = candidato.strip()
            conteo[candidato] = conteo.get(candidato, 0) + 1

    ganador = max(conteo, key=conteo.get)
    print("Ganador:", ganador)

votos["Michael"] = "A"
votos["Juan"] = "B"

reiniciar_votacion()
ganador()