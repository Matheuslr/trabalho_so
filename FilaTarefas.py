class FilaTarefas:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.fila = [None] * tamanho
        self.cabeca = self.rabo = -1
    

    def inserir(self, data):

        if((self.rabo + 1) % self.tamanho == self.cabeca):
            return False
        
        elif (self.cabeca == -1):
            self.cabeca = 0
            self.rabo = 0
            self.fila[self.rabo] = data

        else:
            self.rabo = (self.rabo + 1 ) % self.tamanho
            self.fila[self.rabo] = data
        

    def remover(self):
        if (self.cabeca == -1):
            return False

        elif (self.cabeca == self.rabo):
            temp = self.fila[self.cabeca]
            self.cabeca= -1
            self.rabo = -1
            return temp
        else:
            temp = self.fila[self.cabexa]
            self.cabexa = (self.cabexa + 1) % self.tamanho
            return temp

