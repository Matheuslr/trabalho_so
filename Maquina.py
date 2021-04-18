import time, threading

class Maquina:

    def __init__(self, idMaquina):
        self.id = idMaquina
        self.tarefa= 0
        self.emFuncionamento = False
        self.lock = threading.Lock()
    

    def setTarefa(self, tarefa):
      self.tarefa = tarefa


    def inserirTarefaNaMaquina(self, tarefa):
        if not self.emFuncionamento:
            self.emFuncionamento = True
            t = threading.Thread(target = self.executarTarefa, args=[tarefa])
            t.start()
        else:
            print(f"Maquina {self.id} ocupada")


    def executarTarefa(self, tarefa):
        with self.lock:
          time.sleep(self.tarefa/1000)
          print(f"{self.id}, {tarefa['funcionario']}, {tarefa['descricao'].split(' ')[0]}, {self.tarefa}")
        self.emFuncionamento = False