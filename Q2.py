def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    # Dividir a lista ao meio
    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    # Recursivamente ordenar as duas metades
    esquerda_ordenada = merge_sort(esquerda)
    direita_ordenada = merge_sort(direita)

    # Combinar as duas metades ordenadas
    return merge(esquerda_ordenada, direita_ordenada)


def merge(esquerda, direita):
    resultado = []
    indice_esquerda = 0
    indice_direita = 0

    # Comparar elementos das duas listas e adicionar ao resultado o menor
    while indice_esquerda < len(esquerda) and indice_direita < len(direita):
        if esquerda[indice_esquerda] < direita[indice_direita]:
            resultado.append(esquerda[indice_esquerda])
            indice_esquerda += 1
        else:
            resultado.append(direita[indice_direita])
            indice_direita += 1

    # Adicionar os elementos restantes da lista esquerda, se houver
    while indice_esquerda < len(esquerda):
        resultado.append(esquerda[indice_esquerda])
        indice_esquerda += 1

    # Adicionar os elementos restantes da lista direita, se houver
    while indice_direita < len(direita):
        resultado.append(direita[indice_direita])
        indice_direita += 1

    return resultado

