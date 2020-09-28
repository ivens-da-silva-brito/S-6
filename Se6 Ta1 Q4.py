num= int(input())
pal= str(num)
cont = len(pal)
palInv=""
while cont!=0:
    palInv+=pal[cont -1]
    cont-=1
print (int(palInv))
