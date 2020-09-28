cont= 0
total = 0
while True:
    numero = int(input())
    cont += 1
    total += numero
    if numero ==0:
        cont-=1
        break
if cont ==0:
    print("nao houv numero valido")
else:
    print(total/cont)
