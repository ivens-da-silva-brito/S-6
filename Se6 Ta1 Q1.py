valorDepositado = int(input())
juros = int(input())
juros = juros * 0.01
valorConta = valorDepositado
qtd = 0

while valorConta < valorDepositado * 2 :
    valorConta += valorConta * juros 
    qtd += 1
    
print(qtd)

