class testewith:
    def __enter__(self):
        print('Entrei no contexto')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Estou saindo do contexto')

with testewith() as teste:
    ins = testewith()
    
class Circo:
    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()

class Malabarista:
    def apresentar_show(self):
        print('Malabarista apresentando show')

class Palhaco:
    def apresentar_show(self):
        print('Palhaço apresentando show')


circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()

# circo.apresentar(malabarista)

class Boneca:
    def __init__(self) -> None:
        self.__cordaboneca = 'Branca'

    def cordaboneca(self):
        print(self.__cordaboneca)

# boneca = Boneca()
# boneca.cordaboneca()

# print(dir(Circo))

class Pessoa:
    def __init__(self, nome,cpf) -> None:
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoa):
    def __init__(self,id_cliente,nome,cpf) -> None:
        super().__init__(nome,cpf)
        self.id_cliente = id_cliente

c1 = Cliente(1,321,"levy")

        