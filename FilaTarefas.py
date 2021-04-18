class FilaTarefas:
    
    def __init__(self, tamanho):
        self.fila = []
    

    def inserir(self, data):
        self.fila.append(data)


    def remover(self):
        if len(self.fila) < 1:
            return None
        return self.fila.pop(0)


    def getTamanho(self):
        tamanho = 0
        for i in range(len(self.fila)):
            if(self.fila[i] is not False):
                tamanho += 1
        return tamanho
