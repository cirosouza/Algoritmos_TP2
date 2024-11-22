def ordenaPilha(pilha):

    # pilha auxiliar para movimentar os elementos durante a ordenação
    pilha_auxiliar = []

    while pilha:
        # criacao de variavel com o valor do topo da pilha
        temporario = pilha.pop()

        #verifica se o ultimo elemento da pilha auxiliar é maior que o temporario e devolve, caso realmente seja, 
        #para a pilha principal
        while pilha_auxiliar and pilha_auxiliar[-1] > temporario:
            pilha.append(pilha_auxiliar.pop())

        # por fim, coloca o elemento temporario no topo da pilha auxiliar
        pilha_auxiliar.append(temporario)

    return pilha_auxiliar
