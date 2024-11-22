def conta_pedidos_pares(pilha_pedidos):
    quantidade_pedidos_pares = 0

    for pedido in pilha_pedidos:
        if pedido % 2 == 0:
            quantidade_pedidos_pares += 1

    return quantidade_pedidos_pares


