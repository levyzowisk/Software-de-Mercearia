from controller import PessoaController
while True:
    instrucao = input('Digite 1 para cadastrar uma pessoa, digite dois para sair:')

    if instrucao == '1':
        nome = input('Digite seu nome:')
        idade = input('Digitre sua idade:')
        cpf = input('Digite seu cpf:')
        PessoaController.cadastar(nome,idade,cpf)
        

    if instrucao == '2':
        print('Programa encerrado')
        break