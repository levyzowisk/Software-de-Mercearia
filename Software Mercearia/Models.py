# Qual a ideia do Models? Definir a caracteristicas dos dados.
# Como possso organizar o modelo de inserção ou de armazenamento persistente de dados. O models nos ajuda a facilitar a ideia de como posso organizar esses dadosn para armazenamento, seja em um banco de dados  ou até mesmo em um LocalStorage
#No models eu não digo como deve ser feito o armazenamento, mas ela é o molde que o DAO recebe para poder ter um controle e organização na hora de armazenar os dados.

from datetime import datetime
class Categoria:
    def __init__(self,categoria) -> None:
        self.categoria = categoria
    
    def __repr__ (self):
        return f"Categoria: {self.categoria}"

class Produto:
    def __init__(self,nome, valor,categoria: Categoria) -> None:
        self.nome = nome
        self.valor = f"{valor} R$"
        self.categoria = categoria

class Estoque:
    def __init__(self,produto: Produto, quantidade) -> None:
        self.produto = produto
        self.quantidade = f"{quantidade} unidades"

class Venda:
    def __init__(self, itensVendido: Produto, vendedor, comprador, quantidadeVendida, data = datetime.now().strftime("%d/%m/%y")) -> None:
        self.itensVendido = itensVendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = data

class Fornecedor:
    def __init__(self,nome,cnpf,telefone,categoria) -> None:
        self.nome = nome
        self.cnpf = cnpf
        self.telefone = telefone
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self,clt, nome, telefone, cpf, email, endereco) -> None:
        self.clt = clt
        super(Funcionario,self).__init__(nome, telefone, cpf, email, endereco)
