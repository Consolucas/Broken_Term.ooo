with open("palavras.txt", encoding="utf-8") as file:
    palavras = []

    for linha in file.readlines():
        linha = linha.replace('\n', '')
        if len(linha) == 5:
            palavras.append(linha)
        else:
            continue
