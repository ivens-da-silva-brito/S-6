sal = int(input())
div = int(input())
contAno= 0
contMes = 10
while div < sal :
    div += div * 0.15
    contAno += 1
    contMes += 1
    if contMes == 3 :
        sal += sal*0.05
    if contMes == 12 :
        contMes= 1
ano = int(contAno/12)
mes = contAno% 12
print ( ano,"ano e", mes ," meses" )
print(sal,"%.2f" %div)
