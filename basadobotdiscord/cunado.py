from random import choice
def cargarLista(nombre : str):
    lista = []
    with open(f"utilsCunado/{nombre}.txt") as f:
        for i in f.read().splitlines():
            lista.append(i)

    return lista

paises  = cargarLista("paises")
frases  = cargarLista("frases")
nombres = cargarLista("nombres")

def generador_frase(nombreuser):
    frase = choice(frases)
    if choice(range(25)) == 0:
        frase = frase.replace("{insertarnombre}", nombreuser)

    else:
        frase = frase.replace("{insertarnombre}", choice(nombres))
    
    frase = frase.replace("{nombreuser}", nombreuser)
    frase = frase.replace("{pais}", choice(paises))

    if frase[-1] not in [".", "?", "!"]:
        if frase[-1] == ",":
            frase[-1] == "."

        else:
            frase += "."

    elif frase[-2] == ",":
        del frase[-2]

    return frase