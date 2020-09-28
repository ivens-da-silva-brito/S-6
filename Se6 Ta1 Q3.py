num = int(input())
if num!=0:
    maior = num
    menor = num
    while num!=0:
        num = int(input())
        if maior <num and num != 0:
            maior = num
            
        if menor > num and num != 0 :
            menor = num

    print ("maior" , maior)    
    print ("menor" , menor)
else:
    print("nao foi digitado nenhum numero valido")
