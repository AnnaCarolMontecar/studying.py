lista = [] # lista vazia 
frutas = ["maça", "banana","laranja"] # lista com elementos
mistura = [10, "texto", 3.14, True] # lista com tipos mistos
numeros = list (range(1,6)) # lista gerada automaticamente 

for indice in range(0,11): 
    print (indice)
    # for => estrutura de repetição usada qnd se deseja repetir passos em um numero de vezes previamente conhecidos
comando =""
while comando != "sair":
    comando = input ("Digite um comando ('sair' para encerrar )")# lista, tuple- imutavel e ordenavel  , conjunto - set - nao pode ter duplicata e nao ordenavel, e dicionario  
    print("Voce digitou",comando)
    # estrutura de repeticao nao previsivel -> enquanto 

for indice in range(1,11):
    print(indice)
    if(indice == 5):
        break
    print('oi')
# vai printar oi 5 vezes e quebrar/interromper as repetições

for indice in range(1,11):
    print(indice)
    if(indice == 5):
        continue
    print('oi')
# vai printar oi para todos os valores exceto quando o indice for 5 / entre 1 e 11

#Funções -> bloco de cod reutilizavel que executa tarefas especificas, evita repeticao, organiza e modulariza 
# dividir problemas grandes em partes menores
# deixa o codigo mais limpo 


def saudacao(nome):
    #nome da função + (parametro) 
    print("Olá!Seja bem-vindo(a)"+ nome)

saudacao('Maria')
saudacao('João')

def soma(a,b):
    return a + b #retorno da função
resultado = soma(3,5)
print("A soma é:",resultado)



