teste = list()
teste.append('Josué')
teste.append(18)
pessoas = list()
# [:] => Cria uma cópia dos valores, caso não use é criado uma ligação
pessoas.append(teste[:])
# teste[índice] ou teste.clear() para resetar e novamente teste.append()
teste[0] = 'Juliana'
teste[1] = 16
pessoas.append(teste[:])