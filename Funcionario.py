class Funcionario:

    def __init__(self, idFuncionario: String):
        self.idFuncionario = idFuncionario
        self.tarefas = []


    def lerTarefas(self):
        try:
            with open(f'files/{self.idFuncionario}', 'r') as file:
                self.tarefas = file.readlines()
        except Exception as err:
            print (f"funcionário {idFuncionario} não existe.")
    

    def pegarTarefa(self):
        if self.tarefas > 0:
            return self.tarefas.pop(0)
        else:
            print(f"tarefas finalizadas para o usuário {self.idFuncionario}")
