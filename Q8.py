def inverter_fila(fila_pacientes):
    fila_invertida = []
    for i in range(len(fila_pacientes)):
        fila_invertida.append(fila_pacientes.pop(-1))
    
    return fila_invertida

