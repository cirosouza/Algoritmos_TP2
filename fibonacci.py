def funcao3(n):
    if n <= 1:
        return n
    return funcao3(n - 1) + funcao3(n - 2)

print(funcao3(7))