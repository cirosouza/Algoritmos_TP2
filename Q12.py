class TablaHash:
    def __init__(self, tamanho):
        # gera um objeto com um parametro de tamanho e uma lista de listas com "tamanho" listas dentro de outra lista
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        # Gear um indice que fica entre 0 e (self.tamanho - 1)
        # Garante uma distribuição uniforme dos elementos nos diferentes indices permitidos
        return hash(chave) % self.tamanho
    
    def inserir(self, chave, valor):

        indice = self._hash(chave)
        # Busca a chave e caso ja exista, atualiza o valor
        for item in self.tabela[indice]:
            if item[0] == chave:
                item[1] = valor
            print(f"Chave '{chave}' atualizada com valor '{valor}'.")
        
        # Caso a chave nao exista, cria um novo par chave valor
        self.tabela[indice].append([chave,valor])
        print(f"Chave '{chave}' inserida com valor '{valor}'.")


    def buscar(self, chave):

        indice = self._hash(chave)
        # retorna o valor para a chave dada caso exista
        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]
        # retorna None caso não exista chave
        return None

    def remover(self, chave):

        indice = self._hash(chave)
        # remove o item caso a chave , retorna True caso exista sucesso na remoção
        for item in self.tabela[indice]:
            if item[0] == chave:
                self.tabela[indice].remove(item)
                print(f"Chave '{chave}' removida com sucesso.")
                return True
        
        # retorna False caso não exista a chave informada
        print(f"Chave '{chave}' não encontrada.")
        return False
    

