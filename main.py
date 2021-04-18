from Funcionario import Funcionario
from FilaTarefas import FilaTarefas
from Maquina import Maquina
from utils import estaDisponivel, temTarefa

import re

def main():
    listaMaquinas = list()
    listaFuncionarios = list()
    print("\n################# TRABALHO 1 SISTEMAS OPERACIONAIS #################")

    numeroDeMaquinas = int(input("\nDigite o número de máquinas: "))

    for maquina in range(numeroDeMaquinas):
        idMaquina = input("\nDigite o identificador da máquina %i: " %(maquina+1))
        listaMaquinas.append(Maquina(idMaquina))

    tamanhoFila = int(input("\nDigite a capacidade da fila de tarefas: "))

    numFuncionarios = int(input("\nDigite o número de funcionários: "))
    print("\n")

    for funcionarioNumber in range(numFuncionarios):
        funcionario = Funcionario(f"func{funcionarioNumber+1}")
        funcionario.lerTarefas()
        listaFuncionarios.append(funcionario)

    filaTarefas = FilaTarefas(tamanhoFila)

    totalTarefas = 0
    for funcionario in listaFuncionarios:
        totalTarefas += len(funcionario.tarefas)
    
    while filaTarefas.getTamanho() < tamanhoFila:
        for funcionario in listaFuncionarios:
            if (len(funcionario.tarefas) > 0):
                tarefa = {
                    "descricao": funcionario.pegarTarefa(),
                    "funcionario": funcionario.idFuncionario
                }
                filaTarefas.inserir(tarefa)
        if(filaTarefas.getTamanho() == totalTarefas):
            break

    if(filaTarefas.getTamanho() == 0):
        return 0

    while True:
        maquina = estaDisponivel(listaMaquinas)
        if(maquina is not False):
            tarefa = filaTarefas.remover()
            if(tarefa):
                maquina.setTarefa(int(re.sub("(produto[0-9] )", "", tarefa["descricao"])))
                maquina.inserirTarefaNaMaquina(tarefa)
            novaTarefa = temTarefa(listaFuncionarios)
            if not novaTarefa and filaTarefas.getTamanho() == 0:
                break
            filaTarefas.inserir(novaTarefa)
    
if __name__ == '__main__':
    main()