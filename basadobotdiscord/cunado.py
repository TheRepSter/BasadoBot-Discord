from random import choice
def cargarLista(nombre : str):
    lista = []
    with open(f"utilsCunado/{nombre}.txt", "r", encoding="UTF8") as f:
        for i in f.read().splitlines():
            lista.append(i)

    return lista

paises  = cargarLista("paises")
frases  = cargarLista("frases")
nombres = cargarLista("nombres")
links   = cargarLista("links")

def generador_frase(nombreuser):
    frase = choice(frases)
    if choice(range(25)) == 0:
        frase = frase.replace("{insertarnombre}", nombreuser)

    else:
        frase = frase.replace("{insertarnombre}", choice(nombres))
    
    frase = frase.replace("{nombreuser}", nombreuser)
    frase = frase.replace("{pais}", choice(paises))
    frase = frase.replace("{link}", choice(links))
    frase = frase.replace("{br}", "\n\n")

    frase = frase.strip()

    if frase[-1] not in [".", "?", "!"]:
        if frase[-1] == ",":
            frase[-1] == "."

        else:
            frase += "."

    elif frase[-2] == ",":
        del frase[-2]
    
    if "]" not in frase:
        return frase, {}
    newMessage = ""
    inLinkName = False
    inLink = False
    linkName = ""
    linksDict = {}
    for i in frase:
        if inLinkName:
            if i == "]":
                inLinkName = False
                newMessage += linkName
                linksDict[linkName] = ""
            else:
                linkName += i
        elif inLink:
            if i == ")":
                inLink = False
            else:
                linksDict[linkName] += i
        else:
            if i == "[":
                inLinkName = True
                linkName = ""
            elif i == "(":
                inLink = True
            else:
                newMessage += i
    return newMessage, linksDict