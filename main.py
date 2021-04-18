from Funcionario import Funcionario
from FilaTarefas import FilaTarefas
from Maquina import Maquina

listaTarefas = list()

listaMaquinas = list()
listaFuncionarios = list()
print("################# TRABALHO 1 SISTEMAS OPERACIONAIS #################")

numeroDeMaquinas = int(input("\n Digite o número de máquinas "))

for maquina in range(numeroDeMaquinas):
    idMaquina = input("\n Digite o identificador da máquina %i : " %(ma+1))
    listaMaquinas.append(Maquina(idMaquina))

tamanhoFila = int(input("\n Digite a capacidade da fila de tarefas: "))

numFuncionarios = int(input("\n Digite o número de funcionários: "))

for funcionarioNumber in range(numFuncionarios):
    with open(f"func{funcionarioNumber+1}.txt", 'r') as file:
        print(f"Arquivo do funcionario {funcionarioNumber+1}: func{funcionarioNumber+1}.txt")
        funcionario = Funcionario(funcionarioNumber+1)
        listaFuncionarios.append(funcionario)

filaTarefas = FilaTarefas(tamanhoFila)


for funcionario in listaFuncionarios:
    if len(funcionario.tarefa) > 0 :
        while len(filaTarefas) == tamanhoFila:
            tarefa = funcionario.pegarTarefa()


def pegarTarefaDaFila():
    #pegar Primeira Tarefa Da Fila De Tarefas
    #jogar Tarefa Na Maquina
    pegarTarefaDoFuncionario()