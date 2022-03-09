nd,ct = input().split(' ')
ct = int(ct)
ce = 0
nt = int(nd) - ct

k = input().split(' ')

#CHECK SE O NUMERO DE CONTAGEM TEORICA > 0
for i in range(0, ct, 1):
    if i == ct-1:
        if int(k[i]) > 0:
            ce += 1
        break
    if int(k[i]) > 0:
        ce += 1

#CHECK SE O NUMERO O ELEMENTO SEGUINTE AO ULTIMO COLOCADO É IGUAL
for _ in range(nt):
    if k[ct-1] == k[ct] and k[ct-1] != '0':
        ce += 1
        ct += 1 
        
print(ce)