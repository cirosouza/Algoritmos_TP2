lista_inteiros = [562,58,4516,1,56,4,3,3,2,54,784,968,325,3,56,45,56,98,7,45,25,36,5,4,2,5,4,568,96,21,36,4,45,1,526,4,5221]

def ordena_lista_inteiros(lista):
    for i in range(len(lista)):
        for j in range(0, len(lista)-i-1):

            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista

print(ordena_lista_inteiros(lista_inteiros))



