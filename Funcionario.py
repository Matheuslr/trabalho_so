class Funcionario:

    def __init__(self, idFuncionario):
        self.idFuncionario = idFuncionario
        self.tarefas = []


    def getTamanho(self):
        return len(self.tarefas)


    def lerTarefas(self):
        try:
            with open(f'files/{self.idFuncionario}.txt', 'r') as file:
                self.tarefas = file.readlines()

                for index, line in enumerate(self.tarefas):
                    self.tarefas[index] = line.strip()
        except Exception as err:
            print (f"funcionário {self.idFuncionario} não existe.")
    

    def pegarTarefa(self):
        if self.getTamanho() > 0:
            tarefa = self.tarefas.pop(0)
            return tarefa
        else:
            print(f"tarefas finalizadas para o usuário {self.idFuncionario}")
