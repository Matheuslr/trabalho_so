def estaDisponivel(listaMaquinas):
    for maquina in listaMaquinas:
        if (maquina.emFuncionamento == False):
            return maquina
    return False     


def temTarefa(listaFuncionarios):
    for funcionario in listaFuncionarios:
        if(funcionario.getTamanho() != 0):
            return {
                "descricao": funcionario.pegarTarefa(),
                "funcionario": funcionario.idFuncionario
            }
    return False 