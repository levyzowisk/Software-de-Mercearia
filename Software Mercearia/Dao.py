# Dao utiliza models
from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls,categoria: Categoria):
       with open('categoria.txt', 'a')  as arq:
           arq.writelines(categoria)
           arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt','r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))
        
        listacategoria =[]
        for i in cls.categoria:
            # Instânciando Categoria. listacategoria agora recebe instância de Categoria
            listacategoria.append(Categoria(i))

            print(listacategoria)
            
        return listacategoria
        
class DaoProduto:
    @classmethod
    def salvar(cls, produto: Produto):
        with open("produto.txt", "a") as arq:
            arq.writelines(produto.nome + "|" + produto.valor + "|" + produto.categoria.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open("produto.txt", "r") as arq:
            cls.produto = arq.readlines
            cls.produto = list(map(lambda x: x.replace('\n', ''), cls.produto))
            cls.produto = list(map(lambda x: x.split('|'), cls.produto))
            print(cls.produto)

            listaproduto = []
            for i in cls.produto:
                listaproduto.append(i)
    
            return listaproduto

class Daoestoque:
    @classmethod
    def salvar(cls, estoque: Estoque):
        with open("estoque.txt", 'a') as arq:
            arq.writelines(estoque.produto.nome + "|" + str(estoque.produto.valor) + "|" + estoque.produto.categoria.categoria + "|" + estoque.quantidade)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open("estoque.txt", "r") as arq:
            cls.estoque = arq.readlines()
            # print(cls.estoque[0])
        
        #Substituindo "\n" por ""
        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        print(cls.estoque)
        # print(cls.estoque[0][1])

        listaestoque = []
        for i  in cls.estoque:
            listaestoque.append(i)

        return listaestoque

class DaoVenda:
    @classmethod
    def salvar(cls, venda:Venda):
        with open ('venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendido.nome + "|" + venda.itensVendido.valor + "|" + venda.itensVendido.categoria + "|" + venda.vendedor + "|" + venda.comprador + "|" + str(venda.quantidadeVendida) + "|" + venda.data) 
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
           cls.venda = arq.readlines()
           cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda)) 
           cls.venda = list(map(lambda x: x.split('|'), cls.venda)) 

           print(cls.venda)
           listavenda = [] 
           for i in cls.venda:
               listavenda.append(i)

           return listavenda

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open("fornecedor.txt", "a") as arq:
            arq.writelines(fornecedor.nome + "" + fornecedor.cnpf + "" + fornecedor.telefone + "" + fornecedor.categoria)
            arq.writelines("\n")

    @classmethod
    def ler(cls):
        with open("fornecedor.txt", "r") as arq:
            cls.fornecedor = arq.readlines()
            cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor)) 
            cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))

            print(cls.fornecedor)

            listafornecedor = []
            for i in cls.fornecedor:
                listafornecedor.append(i)
            return listafornecedor

class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open("pessoa.txt", "a") as arq:
            arq.writelines(pessoa.nome + "" + pessoa.telefone + "" + pessoa.cpf + "" + pessoa.email + "" + pessoa.endereco)
            arq.writelines("\n")

    @classmethod
    def ler(cls):
        with open("fornecedor.txt", "r") as arq:
            cls.pessoa = arq.readlines()
            cls.pessoa = list(map(lambda x: x.replace('\n', ''), cls.pessoa)) 
            cls.pessoa = list(map(lambda x: x.split('|'), cls.pessoa)) 

            print(cls.pessoa)

            listapessoa = []
            for i in cls.pessoa:
                listapessoa.append(i)
            return listapessoa

class DaoFuncionario:
    @classmethod
    def salvar(cls,funcionario:Funcionario):
        with open("funcionario.txt", "a") as arq:
            arq.writelines(funcionario.clt + " " + funcionario.nome + " " + funcionario.telefone + " " + funcionario.cpf + " " + funcionario.email + " " + funcionario.endereco)
            arq.writelines("\n")

    @classmethod
    def ler(cls):
        with open("funcionario.txt", "r") as arq:
            cls.funcionario = arq.readlines()
            cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario)) 
            cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario)) 

            print(cls.funcionario)

            listafuncionario = []
            for i in listafuncionario:
                listafuncionario.append(i)
            return listafuncionario

# c = Categoria('Moda Masculina')
# p = Produto('Brim', 50.0, c)

# e = Estoque(p,15)


# DaoCategoria.salvar(p)
# DaoCategoria.ler()

# itens = [['Brim', '50.0 R$', 'Moda Masculina', '15 unidades'], ['levy']]
# print(itens[0].[1])

# D = DaoCategoria()
# # D.salvar('Quentes')
# D.ler()

    