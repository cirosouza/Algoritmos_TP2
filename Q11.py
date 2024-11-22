class FilaAtendimento:
    def __init__(self):

        self.fila = list()


    def adicionar_cliente(self, nome):

        self.fila.append(nome)
        print(f"Cliente {nome} adicionado à fila.")
    
    def atender_cliente(self):

        if not self.fila:
            print("Nenhum cliente na fila para atender.")
            return None
        cliente_atendido = self.fila.pop(0)
        print(f"Cliente {cliente_atendido} está sendo atendido.")
        return cliente_atendido
    
    def tamanho_fila(self):

        return len(self.fila)
    

# Criando a fila de atendimento
fila = FilaAtendimento()

# Adicionando clientes à fila
fila.adicionar_cliente("João")
fila.adicionar_cliente("Maria")
fila.adicionar_cliente("Ana")

# Exibindo o tamanho da fila
print("Tamanho da fila:", fila.tamanho_fila())

# Atendendo os clientes
fila.atender_cliente()
fila.atender_cliente()

# Exibindo o tamanho da fila após atendimentos
print("Tamanho da fila:", fila.tamanho_fila())

# Atendendo o último cliente
fila.atender_cliente()

# Tentando atender um cliente quando a fila está vazia
fila.atender_cliente()

