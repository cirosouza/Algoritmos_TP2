def encontraDuplicadosForcaBruta(lista):
    lista_duplicados = []

    for i in range(len(lista)):
        elemento = lista[i]

        for j in range(len(lista)):
            if ((elemento == lista[j]) and i != j):
                lista_duplicados.append(lista[j])


    return lista_duplicados
        

def encontraDuplicadosEficiente(lista):
    conjunto_avaliados = set()
    duplicados = set()

    for elemento in lista:
        if elemento in conjunto_avaliados:
            duplicados.add(elemento)
        else:
            conjunto_avaliados.add(elemento)

    return list(duplicados)


