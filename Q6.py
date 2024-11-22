def conta_pedidos_impares(pilha_pedidos):
    quantidade_pedidos_impares = 0

    for pedido in pilha_pedidos:
        if pedido % 2 != 0:
            quantidade_pedidos_impares += 1

    return quantidade_pedidos_impares


