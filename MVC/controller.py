from dal import PessoaDal
from models import Pessoa
class PessoaController:
    @classmethod
    def cadastar(cls,nome,idade,cpf):
        # Irei implementar minhas Regras de negócio.
        if PessoaController.validar(nome,idade,cpf):
            PessoaDal.salvar(Pessoa(nome,idade,cpf))

        else:
            print("Campos inválidos")

    @classmethod
    def validar(cls,nome,idade,cpf):
        if len(nome) >= 4 and (int(idade) > 0 and int(idade) < 150) and len(cpf) == 11:
            return True
        return False