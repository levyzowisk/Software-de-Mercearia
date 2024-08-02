from models import Pessoa
class PessoaDal:
    @classmethod
    def salvar(cls,pessoa):
        with open('pessoas.txt', 'a') as arq:
            arq.write(pessoa.nome + " " + str(pessoa.idade) + " " + str(pessoa.cpf) + "\n")