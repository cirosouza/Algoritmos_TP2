def contar_livros_impares(lista_livros):
    quantidade_impares = 0

    for livro in lista_livros:
        if livro % 2 != 0:  
            quantidade_impares += 1

    return quantidade_impares

