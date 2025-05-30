nome = 'Agatha'
sobrenome = "Moura"
print(nome)

idade = 17
verdadeiro = True
falso = False
frutas = ['maça', 'banana', 'laranja']
pi = 3.1415

class Pessoa:
    #construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

pessoa = Pessoa(nome, idade)
pessoa.apresentar()

if(verdadeiro):
    print('Verdadeiro')

else:
    print('Falso')

while(idade<18):
    print('Idade: ', idade)
    break

if(verdadeiro):
    pass

for fruta in frutas:
    print('Fruta: ', fruta)

def funcao():
    print('função executada')

funcao()



dicionario = { 
    'Aluno 1' : "Ana",
    'Aluno 2' :"Joao",
    0: "Valor 0",
    'frutas' : frutas
}

print(dicionario['Aluno 1'])

array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

tupla = ('maça', 'maracuja')
nome_completo = f'{pessoa.nome} {sobrenome}'
print(nome_completo)


##OPERADORES LÓGICOS são escritos : and, or
##OPERADORES NORMAIS : % , / , +, - +=, ==, ===, 
if(pi > 3):
    print('valor maaior que 3 : {pi}')

print('fim')
