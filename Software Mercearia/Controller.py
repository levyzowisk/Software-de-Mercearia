from Models import *
from Dao import  *

from datetime import  datetime

# Importante destacar que, antes da inserção de um novo conteúdo no arquivo é necessário verificar se esse registro  já existe no Categoria.txt
class ControllerCategoria:
    
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        # Posso implementar uma função que coloca em caixa baixa as letras que tem no arquivo e as que estão sendo enseridas e verifica se são iguais...
        for i in x:
            if i.categoria == novaCategoria:
                # print(i.categoria)
                existe = True
            
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria Cadastrada com sucesso')
        else:
            print('A categoria previamente cadastrada.')


i = ControllerCategoria()
i.cadastraCategoria('Frios')