import time, threading

class Maquina:

    def __init__(self, idMaquina):
        self.id = idMaquina
        self.tarefa= 0
        self.emFuncionamento = False
        self.lock = threading.Lock()
    

    def setTarefa(self, tarefa):
      self.tarefa = tarefa


    def inserirTarefaNaMaquina(self, nomeTarefa):
        if not self.emFuncionamento:
            t = threading.Thread(target = self.executarTarefas, args=[nomeTarefa])
            t.start()
            t.join()
        else:
            print(f"Maquina {self.id} ocupada")


    def executarTarefa(self, nomeTarefa):
        with self.lock:
          time.sleep(self.tarefa/1000)
          print(f"A tarefa '{nomeTarefa}' foi concluida")
